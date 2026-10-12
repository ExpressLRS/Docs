"""Git revision dates and GitHub committers for Zensical.

Zensical has no plugin API yet, but every page still goes through Python
Markdown, and the page metadata dict handed to extensions is what Rust reads
back for the templates. So this is a Markdown extension that does the work of
mkdocs-git-revision-date-localized-plugin and mkdocs-git-committers-plugin-2:

  page.meta.git_revision_date_localized   last commit touching the file
  page.meta.git_creation_date_localized   first commit (follows renames)
  page.meta.git_committers                [{login, name, url, avatar}, ...]

The stock partials/source-file.html already renders the two dates. The
committers need a one-line override, since the stock template reads a
top-level `committers` variable that only the MkDocs plugin could set.

zensical.toml:

  [project.markdown_extensions.git_info]
  repository = "ExpressLRS/Docs"
  branch = "master"
  docs_dir = "docs"
  type = "date"          # date | datetime | iso_date | iso_datetime | timeago
  locale = "en"
  committers = true
  cache_file = ".git-committers.json"

Committer logins come from the GitHub API (one call per unknown author, cached
in cache_file). Set GITHUB_TOKEN, or MKDOCS_GIT_COMMITTERS_APIKEY, in CI.
Without a token it uses whatever is cached plus noreply addresses, and skips
the rest rather than failing the build. The checkout needs full history
(actions/checkout with fetch-depth: 0), or every page looks a day old.
"""

from __future__ import annotations

import atexit
import http.client
import json
import logging
import os
import re
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from markdown import Extension, Markdown
from markdown.preprocessors import Preprocessor

try:
    from babel.dates import format_date, format_datetime
except ImportError:  # babel is optional, dates fall back to strftime
    format_date = format_datetime = None


NOREPLY = re.compile(r"^(?:\d+\+)?([^@]+)@users\.noreply\.github\.com$")


log = logging.getLogger(__name__)


def git(*args: str, cwd: Path | None = None) -> str:
    # safe.directory: the repo is often a bind mount owned by someone else
    return subprocess.run(
        ["git", "-c", "safe.directory=*", *args],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


# ----------------------------------------------------------------------------
# Git history and the committer cache, shared across every page render
# ----------------------------------------------------------------------------


class History:
    def __init__(self, cfg: dict[str, Any]):
        self.cfg = cfg
        self.lock = threading.Lock()
        self.commits: dict[str, list[tuple[int, str, str, str]]] = {}
        try:
            self.root = Path(git("rev-parse", "--show-toplevel").strip())
        except (OSError, subprocess.CalledProcessError) as e:
            # No git, not a checkout, or a bind mount git refuses to trust:
            # build without dates rather than not at all
            log.warning("git_info: no git history, skipping (%s)", e)
            self.root = None
        self.cache_path = Path(cfg["cache_file"])
        self.users: dict[str, dict | None] = {}
        self.dirty = False
        self.token = os.environ.get("MKDOCS_GIT_COMMITTERS_APIKEY") or os.environ.get(
            "GITHUB_TOKEN"
        )
        self.api_dead = False
        if self.cache_path.exists():
            try:
                self.users = json.loads(self.cache_path.read_text())["users"]
            except (ValueError, KeyError):
                pass
        atexit.register(self.save)
        if self.root is None:
            return
        self.index()
        if cfg["committers"]:
            self.prefetch()

    def index(self) -> None:
        """Read the whole docs history in one git call, following renames.

        One subprocess per page is ~100ms each under build load; this is one
        call for the lot. Walking newest to oldest, a rename maps the old
        name onto whatever the file is called at HEAD.
        """
        self.docs = (
            (Path.cwd() / self.cfg["docs_dir"])
            .resolve()
            .relative_to(self.root.resolve())
            .as_posix()
        )
        out = git(
            "log",
            "--no-merges",
            "-M",
            "--name-status",
            "--format=%x00%at%x1f%an%x1f%ae%x1f%H",
            "--",
            self.docs,
            cwd=self.root,
        )
        alias: dict[str, str] = {}
        for chunk in out.split("\0")[1:]:
            head, *files = chunk.strip("\n").split("\n")
            t, name, email, sha = head.split("\x1f")
            commit = (int(t), name, email.lower(), sha)
            for line in files:
                if not line:
                    continue
                status, *paths = line.split("\t")
                current = alias.get(paths[-1], paths[-1])
                self.commits.setdefault(current, []).append(commit)
                if status.startswith("R"):
                    alias[paths[0]] = current

    def log(self, path: str) -> list[tuple[int, str, str, str]]:
        """Commits touching a docs-relative path, newest first."""
        if self.root is None:
            return []
        return self.commits.get(f"{self.docs}/{path}", [])

    def prefetch(self) -> None:
        """Resolve every author up front, in parallel.

        Lookups are a few hundred ms each and page renders are serial, so
        doing them lazily turns a cold cache into minutes of build time.
        """
        todo: dict[str, tuple[str, str]] = {}
        for commits in self.commits.values():
            for _, name, email, sha in commits:
                if email not in self.users and email not in todo:
                    todo[email] = (name, sha)
        if todo:
            with ThreadPoolExecutor(8) as pool:
                for email, (name, sha) in todo.items():
                    pool.submit(self.user, email, name, sha)

    def user(self, email: str, name: str, sha: str) -> dict | None:
        with self.lock:
            if email in self.users:
                return self.users[email]
        user = None
        if m := NOREPLY.match(email):
            user = self._profile(m.group(1), name)
        elif not self.api_dead:
            data = self._api(f"repos/{self.cfg['repository']}/commits/{sha}")
            if data and data.get("author"):
                a = data["author"]
                user = {
                    "login": a["login"],
                    "name": name,
                    "url": a["html_url"],
                    "avatar": a["avatar_url"],
                }
            elif data is None:
                return None  # API failure, don't cache a negative
        with self.lock:
            self.users[email] = user
            self.dirty = True
        return user

    def _profile(self, login: str, name: str) -> dict:
        return {
            "login": login,
            "name": name,
            "url": f"https://github.com/{login}",
            "avatar": f"https://avatars.githubusercontent.com/{login}",
        }

    def _api(self, path: str) -> dict | None:
        req = urllib.request.Request(
            f"https://api.github.com/{path}",
            headers={"Accept": "application/vnd.github+json"},
        )
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        try:
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 429):  # bad token or rate limited
                self.api_dead = True
            return {} if e.code == 422 else None  # 422: sha not on GitHub
        except (OSError, http.client.HTTPException, ValueError):
            return None  # flaky network shouldn't fail the build

    def save(self) -> None:
        if not self.dirty:
            return
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache_path.write_text(
            json.dumps({"users": self.users}, indent=1, sort_keys=True)
        )


_history: History | None = None
_history_lock = threading.Lock()


def history(cfg: dict[str, Any]) -> History:
    global _history
    with _history_lock:
        if _history is None:
            _history = History(cfg)
        return _history


# ----------------------------------------------------------------------------
# The Markdown side
# ----------------------------------------------------------------------------


def render_date(ts: int, cfg: dict[str, Any]) -> str:
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    kind, locale = cfg["type"], cfg["locale"]
    if kind == "timeago":
        # Readable date as the no-JS fallback; assets/javascripts/timeago.js
        # swaps it for "3 months ago"
        return (
            f'<span class="timeago" datetime="{dt.isoformat()}" '
            f'title="{dt.strftime("%Y-%m-%d")}">'
            f"{render_date(ts, {**cfg, 'type': 'date'})}</span>"
        )
    if kind == "iso_date":
        return dt.strftime("%Y-%m-%d")
    if kind == "iso_datetime":
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    if kind == "datetime":
        if format_datetime:
            return format_datetime(dt, format="medium", locale=locale)
        return dt.strftime("%B %d, %Y %H:%M:%S")
    if format_date:
        return format_date(dt, format="long", locale=locale)
    return dt.strftime("%B %d, %Y")


class GitInfoPreprocessor(Preprocessor):
    def __init__(self, md: Markdown, cfg: dict[str, Any]):
        super().__init__(md)
        self.cfg = cfg

    def run(self, lines: list[str]) -> list[str]:
        # Imported late so this module can be loaded outside Zensical
        from zensical.extensions.context import ContextPreprocessor

        ctx = ContextPreprocessor.from_markdown(self.md)
        if ctx is None:
            return lines
        page = ctx.page
        hist = history(self.cfg)
        commits = hist.log(page.path)
        if hist.root is None:
            return lines
        if not commits:  # untracked file: say "now", like the MkDocs plugin
            now = int(datetime.now(tz=timezone.utc).timestamp())
            commits = [(now, "", "", "")]

        meta = page.meta
        meta.setdefault(
            "git_revision_date_localized", render_date(commits[0][0], self.cfg)
        )
        meta.setdefault(
            "git_creation_date_localized", render_date(commits[-1][0], self.cfg)
        )

        if self.cfg["committers"] and commits[0][3]:
            # Most commits first, matching mkdocs-git-committers-plugin-2
            counts: dict[str, list] = {}
            for _, name, email, sha in commits:
                entry = counts.setdefault(email, [0, name, sha])
                entry[0] += 1
            seen, people = set(), []
            for email, (_, name, sha) in sorted(
                counts.items(), key=lambda kv: -kv[1][0]
            ):
                user = hist.user(email, name, sha)
                if (
                    user
                    and user["login"] not in seen
                    and user["login"] not in self.cfg["exclude"]
                ):
                    seen.add(user["login"])
                    people.append(user)
            meta["git_committers"] = people
        return lines


class GitInfoExtension(Extension):
    def __init__(self, **kwargs: Any):
        self.config = {
            "repository": ["", "owner/name on GitHub, for committer lookup"],
            "branch": ["master", "unused for now, kept for parity"],
            "docs_dir": ["docs", "docs dir relative to the repo root"],
            "type": ["date", "date | datetime | iso_date | iso_datetime | timeago"],
            "locale": ["en", "babel locale for date formatting"],
            "committers": [True, "resolve GitHub committers"],
            "exclude": [[], "logins to leave out, e.g. bots"],
            "cache_file": [".git-committers.json", "login cache"],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: Markdown) -> None:
        # Below Zensical's context preprocessor (priority 0) is irrelevant,
        # it's looked up by type, but stay ahead of front-matter stripping.
        md.preprocessors.register(
            GitInfoPreprocessor(md, self.getConfigs()), "git_info", 5
        )


def makeExtension(**kwargs: Any) -> GitInfoExtension:
    return GitInfoExtension(**kwargs)
