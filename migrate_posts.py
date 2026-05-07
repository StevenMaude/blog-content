#!/usr/bin/env python3
"""Migrate Pelican blog posts to Hugo format."""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path("/home/runner/work/blog-content/blog-content")
POSTS_SRC = REPO_ROOT / "posts"
PAGES_SRC = REPO_ROOT / "pages"
CONTENT_POSTS = REPO_ROOT / "content" / "posts"


def parse_pelican_meta(lines):
    """Parse Pelican metadata lines into a dict, returning (meta, body_start_idx).

    Handles multi-line values: continuation lines start with whitespace.
    """
    meta = {}
    last_key = None
    i = 0
    for i, line in enumerate(lines):
        line = line.rstrip("\n")
        if line.strip() == "":
            break
        # Continuation line (indented) - append to last key
        if last_key and line.startswith((" ", "\t")):
            meta[last_key] = (meta[last_key] + " " + line.strip()).strip()
            continue
        # Pelican metadata: Key: Value
        m = re.match(r"^([A-Za-z]+):\s*(.*)", line)
        if m:
            last_key = m.group(1).strip()
            meta[last_key] = m.group(2).strip()
        else:
            # Not metadata anymore - content started without blank line
            break
    return meta, i + 1


def convert_date(date_str):
    """Convert '2013-05-11 12:55' to '2013-05-11T12:55:00+00:00'."""
    date_str = date_str.strip()
    # Handle formats like '2013-05-11 12:55' or '2013-05-11 12:55:00'
    m = re.match(r"^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}(?::\d{2})?)$", date_str)
    if m:
        d = m.group(1)
        t = m.group(2)
        if len(t) == 5:
            t += ":00"
        return f"{d}T{t}+00:00"
    # Already ISO format
    return date_str


def yaml_escape(s):
    """Escape a string for YAML, using quotes if needed."""
    # Check if needs quoting
    if any(c in s for c in [':', '#', '"', "'", '{', '}', '[', ']', '&', '*', '!', '|', '>', '%', '@', '`']):
        # Use double quotes, escape inner double quotes
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    # Check if it starts with special chars or is a boolean/null/number
    if re.match(r'^[>|{}\[\],#&*!|\'"%@`]', s) or s.lower() in ('true', 'false', 'null', 'yes', 'no'):
        return f'"{s}"'
    return s


def convert_body(body, year=None):
    """Convert Pelican-specific syntax in body to Hugo syntax."""
    # Convert {filename}../YEAR/post-name.md links
    # Pattern: [text]({filename}../YEAR/post-name.md)
    def replace_filename(m):
        text = m.group(1)
        path = m.group(2)
        # Extract YEAR/post-name.md from ../YEAR/post-name.md
        path_m = re.match(r"\{filename\}\.\.\/(\d{4})\/(.+\.md)", path)
        if path_m:
            yr = path_m.group(1)
            fname = path_m.group(2)
            return f'[{text}]({{{{< ref "/posts/{yr}/{fname}" >}}}})'
        # Same year: {filename}post-name.md
        path_m2 = re.match(r"\{filename\}(.+\.md)", path)
        if path_m2 and year:
            fname = path_m2.group(1)
            return f'[{text}]({{{{< ref "/posts/{year}/{fname}" >}}}})'
        return m.group(0)

    body = re.sub(r'\[([^\]]+)\]\((\{filename\}[^)]+)\)', replace_filename, body)

    # Convert {static}/images/ -> /images/
    body = body.replace("{static}/images/", "/images/")

    return body


def build_front_matter(meta, filename_stem):
    """Build Hugo YAML front matter from Pelican metadata dict."""
    lines = ["---"]

    # Title
    title = meta.get("Title", filename_stem)
    lines.append(f"title: {yaml_escape(title)}")

    # Date
    if "Date" in meta:
        lines.append(f"date: {convert_date(meta['Date'])}")

    # Modified -> lastmod
    if "Modified" in meta:
        lines.append(f"lastmod: {convert_date(meta['Modified'])}")

    # Author
    if "Author" in meta:
        lines.append(f"author: {yaml_escape(meta['Author'])}")

    # Tags
    if "Tags" in meta:
        tags = [t.strip() for t in meta["Tags"].split(",") if t.strip()]
        tags_str = ", ".join(f'"{t}"' for t in tags)
        lines.append(f"tags: [{tags_str}]")

    # Slug
    slug = meta.get("Slug", filename_stem)
    lines.append(f"slug: {yaml_escape(slug)}")

    # Summary -> description
    if "Summary" in meta:
        lines.append(f"description: {yaml_escape(meta['Summary'])}")

    # Alias -> aliases
    if "Alias" in meta:
        alias = meta["Alias"].strip()
        lines.append(f"aliases: [\"{alias}\"]")

    lines.append("---")
    return "\n".join(lines) + "\n"


def migrate_post(src_path, year):
    """Migrate a single Pelican post file."""
    with open(src_path, "r", encoding="utf-8") as f:
        raw = f.read()

    lines = raw.split("\n")
    meta, body_start = parse_pelican_meta(lines)

    if not meta:
        print(f"WARNING: No metadata found in {src_path}", file=sys.stderr)
        return

    body = "\n".join(lines[body_start:])
    body = convert_body(body, year=year)

    filename_stem = src_path.stem
    front_matter = build_front_matter(meta, filename_stem)

    # Output path
    out_dir = CONTENT_POSTS / year
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / src_path.name

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write(body)

    return out_path


def migrate_page(src_path):
    """Migrate the about page."""
    with open(src_path, "r", encoding="utf-8") as f:
        raw = f.read()

    lines = raw.split("\n")
    meta, body_start = parse_pelican_meta(lines)
    body = "\n".join(lines[body_start:])
    body = convert_body(body)

    filename_stem = src_path.stem
    front_matter = build_front_matter(meta, filename_stem)

    slug = meta.get("Slug", filename_stem)
    out_dir = REPO_ROOT / "content" / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.md"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write(body)

    return out_path


def main():
    count = 0
    errors = 0

    # Migrate posts
    for year_dir in sorted(POSTS_SRC.iterdir()):
        if not year_dir.is_dir():
            continue
        year = year_dir.name
        if not re.match(r"^\d{4}$", year):
            continue
        for post_file in sorted(year_dir.glob("*.md")):
            try:
                out = migrate_post(post_file, year)
                if out:
                    print(f"  Migrated: posts/{year}/{post_file.name}")
                    count += 1
            except Exception as e:
                print(f"ERROR migrating {post_file}: {e}", file=sys.stderr)
                errors += 1

    # Migrate pages
    about_page = PAGES_SRC / "about_me.md"
    if about_page.exists():
        try:
            out = migrate_page(about_page)
            print(f"  Migrated: pages/about_me.md -> {out.relative_to(REPO_ROOT)}")
            count += 1
        except Exception as e:
            print(f"ERROR migrating about page: {e}", file=sys.stderr)
            errors += 1

    print(f"\nMigration complete: {count} files migrated, {errors} errors.")


if __name__ == "__main__":
    main()
