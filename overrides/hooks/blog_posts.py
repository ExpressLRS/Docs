"""Hook to inject recent blog posts into the homepage context."""

import os
import yaml
import datetime


def on_page_context(context, page, config, nav):
    """Inject recent blog posts into the homepage template context."""
    if page.file.src_path != "index.md":
        return context

    posts_dir = os.path.join(config["docs_dir"], "blog", "posts")
    if not os.path.isdir(posts_dir):
        return context

    posts = []
    for filename in os.listdir(posts_dir):
        if not filename.endswith(".md"):
            continue
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse front matter
        if not content.startswith("---"):
            continue
        end = content.index("---", 3)
        front_matter = yaml.safe_load(content[3:end])

        title = front_matter.get("title", "Untitled")
        post_date = front_matter.get("date")
        slug = front_matter.get("slug", filename.replace(".md", ""))

        # Normalize date to datetime.date
        if isinstance(post_date, str):
            post_date = datetime.datetime.strptime(post_date, "%Y-%m-%d").date()
        elif isinstance(post_date, datetime.datetime):
            post_date = post_date.date()
        elif isinstance(post_date, datetime.date):
            pass  # already a date
        else:
            continue

        # Build URL matching mkdocs-material blog plugin URL pattern
        date_path = post_date.strftime("%Y/%m/%d")
        url = f"blog/{date_path}/{slug}/"

        categories = front_matter.get("categories", [])

        posts.append({
            "title": title,
            "date": post_date,
            "date_formatted": post_date.strftime("%B %d, %Y"),
            "url": url,
            "category": categories[0] if categories else None,
        })

    # Sort by date descending, take latest 3
    posts.sort(key=lambda p: p["date"], reverse=True)
    context["recent_posts"] = posts[:3]

    return context
