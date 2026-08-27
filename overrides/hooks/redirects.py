"""Generate static redirect pages from redirects.yml.

Under mkdocs the mkdocs-redirects plugin consumes redirects.yml (via
INHERIT) and writes meta-refresh stub pages. Zensical has no redirects
support yet, so this standalone script does the same thing — run it
after the site has been built:

    python3 overrides/hooks/redirects.py
"""

import html
import os
import yaml

STUB = """\
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex">
    <link rel="canonical" href="{url}">
    <meta http-equiv="refresh" content="0; url={url}">
    <title>Redirecting…</title>
  </head>
  <body>
    Redirecting to <a href="{url}">{url}</a>…
    <script>location.replace("{url}");</script>
  </body>
</html>
"""


def _src_to_dir(src_path):
    """Map an old source path to its pretty-URL output directory."""
    path = src_path.replace("\\", "/")
    if path.endswith("/index.md"):
        return path[: -len("index.md")]
    if path == "index.md":
        return ""
    return path[: -len(".md")] + "/" if path.endswith(".md") else path


def _target_to_url(target, site_url):
    """Map a redirect target (external URL or source path) to a URL."""
    if target.startswith(("http://", "https://")):
        return target
    path, anchor = (target.split("#", 1) + [""])[:2]
    url = site_url + _src_to_dir(path)
    return f"{url}#{anchor}" if anchor else url


def main(repo_root):
    with open(os.path.join(repo_root, "redirects.yml"), encoding="utf-8") as f:
        redirect_maps = yaml.safe_load(f)["plugins"]["redirects"]["redirect_maps"]

    import tomllib
    with open(os.path.join(repo_root, "zensical.toml"), "rb") as f:
        site_url = tomllib.load(f)["project"]["site_url"].rstrip("/") + "/"

    site_dir = os.path.join(repo_root, "site")
    if not os.path.isdir(site_dir):
        raise SystemExit("redirects: site/ not found — build the site first")

    count = 0
    for src, target in redirect_maps.items():
        out_dir = os.path.join(site_dir, _src_to_dir(src))
        out_path = os.path.join(out_dir, "index.html")
        if os.path.exists(out_path):
            print(f"redirects: skipping {src} — a real page exists at {out_path}")
            continue
        url = html.escape(_target_to_url(target, site_url), quote=True)
        os.makedirs(out_dir, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(STUB.format(url=url))
        count += 1

    print(f"redirects: wrote {count} redirect stubs to {site_dir}")


if __name__ == "__main__":
    main(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
