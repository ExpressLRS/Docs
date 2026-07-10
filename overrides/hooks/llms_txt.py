"""Hook to generate llms.txt at build time from the nav configuration."""

import os
import yaml


def on_post_build(config, **kwargs):
    """Generate llms.txt in the site output directory."""
    site_name = config["site_name"]
    site_url = config["site_url"].rstrip("/") + "/"
    site_description = config.get("site_description", "")
    docs_dir = config["docs_dir"]
    site_dir = config["site_dir"]

    lines = []
    lines.append(f"# {site_name}")
    lines.append("")
    if site_description:
        lines.append(f"> {site_description}")
        lines.append("")

    for item in config["nav"]:
        if isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    # Top-level page (e.g., Home, FAQ)
                    url = _make_url(site_url, value)
                    desc = _get_description(docs_dir, value)
                    lines.append(f"## {title}")
                    lines.append("")
                    lines.append(_format_link(title, url, desc))
                    lines.append("")
                elif isinstance(value, list):
                    # Section with children
                    lines.append(f"## {title}")
                    lines.append("")
                    _walk_nav(value, site_url, docs_dir, lines)
                    lines.append("")

    output = "\n".join(lines).rstrip() + "\n"
    output_path = os.path.join(site_dir, "llms.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)


def _walk_nav(items, site_url, docs_dir, lines):
    """Recursively walk nav items, emitting link lines for pages."""
    for item in items:
        if isinstance(item, str):
            # Bare path (e.g., blog/index.md used as section index)
            url = _make_url(site_url, item)
            title = _get_title(docs_dir, item)
            if not title:
                # Derive title from directory name or filename
                base = item.replace("\\", "/")
                if base.endswith("/index.md"):
                    title = base.split("/")[-2].replace("-", " ").title()
                else:
                    title = os.path.splitext(os.path.basename(base))[0].replace("-", " ").title()
            desc = _get_description(docs_dir, item)
            lines.append(_format_link(title, url, desc))
        elif isinstance(item, dict):
            for title, value in item.items():
                if isinstance(value, str):
                    url = _make_url(site_url, value)
                    desc = _get_description(docs_dir, value)
                    lines.append(_format_link(title, url, desc))
                elif isinstance(value, list):
                    # Nested section — recurse without adding a new heading
                    _walk_nav(value, site_url, docs_dir, lines)


def _make_url(site_url, src_path):
    """Convert a docs source path to an absolute URL."""
    # index.md -> /
    # quick-start/getting-started.md -> quick-start/getting-started/
    path = src_path.replace("\\", "/")
    if path == "index.md":
        path = ""
    elif path.endswith("/index.md"):
        path = path[: -len("index.md")]
    elif path.endswith(".md"):
        path = path[: -len(".md")] + "/"
    return site_url + path


def _get_front_matter(docs_dir, src_path):
    """Read YAML front matter from a markdown file."""
    filepath = os.path.join(docs_dir, src_path)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, IOError):
        return {}
    if not content.startswith("---"):
        return {}
    try:
        end = content.index("---", 3)
        return yaml.safe_load(content[3:end]) or {}
    except (ValueError, yaml.YAMLError):
        return {}


def _get_description(docs_dir, src_path):
    """Extract the description field from a page's front matter."""
    return _get_front_matter(docs_dir, src_path).get("description")


def _get_title(docs_dir, src_path):
    """Extract the title field from a page's front matter."""
    return _get_front_matter(docs_dir, src_path).get("title")


def _format_link(title, url, description=None):
    """Format a single link line."""
    if description:
        return f"- [{title}]({url}): {description}"
    return f"- [{title}]({url})"
