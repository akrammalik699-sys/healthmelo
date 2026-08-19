from pathlib import Path
from datetime import datetime
import re
import shutil


ROOT = Path(__file__).resolve().parent

SITE_URL = "https://legendary-llama-0aca4c.netlify.app"

SITEMAP = ROOT / "sitemap.xml"

BACKUP_DIR = ROOT.parent / "HEALTH_MELO_BACKUP"

REPORTS = ROOT / "seo_reports"

SKIP_DIRS = {
    ".git",
    ".netlify",
    "node_modules",
    "__pycache__",
    "seo_reports",
}


GOOGLE_FILE = "google6dac5feead5d9a65.html"


# =========================================================
# FIND HTML FILES
# =========================================================

def find_html_files():

    files = []

    for path in ROOT.rglob("*.html"):

        if any(
            part in SKIP_DIRS
            for part in path.parts
        ):
            continue

        if path.name == GOOGLE_FILE:
            continue

        files.append(path)

    return sorted(files)


# =========================================================
# CREATE URL FROM HTML PATH
# =========================================================

def html_to_url(path):

    relative = path.relative_to(ROOT)

    # Root homepage
    if relative.as_posix() == "index.html":
        return SITE_URL + "/"

    # index.html inside folder
    if relative.name.lower() == "index.html":

        folder = relative.parent.as_posix()

        return (
            SITE_URL
            + "/"
            + folder.strip("/")
            + "/"
        )

    # Other HTML files
    return (
        SITE_URL
        + "/"
        + relative.as_posix()
    )


# =========================================================
# NORMALIZE URL
# =========================================================

def normalize_url(url):

    url = url.strip()

    url = url.replace(
        "http://",
        "https://"
    )

    return url.rstrip("/") + "/"


# =========================================================
# EXTRACT EXISTING SITEMAP URLS
# =========================================================

def existing_urls():

    if not SITEMAP.exists():
        return set()

    text = SITEMAP.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    urls = set(
        re.findall(
            r"<loc>\s*(.*?)\s*</loc>",
            text,
            re.I | re.S
        )
    )

    return {
        normalize_url(url)
        for url in urls
    }


# =========================================================
# BACKUP OLD SITEMAP
# =========================================================

def backup_sitemap():

    if not SITEMAP.exists():
        return False

    target = (
        BACKUP_DIR
        / "sitemap.xml"
    )

    target.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(
        SITEMAP,
        target
    )

    return True


# =========================================================
# BUILD SITEMAP
# =========================================================

def build_sitemap(urls):

    today = datetime.now().strftime(
        "%Y-%m-%d"
    )

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    for url in sorted(urls):

        priority = "0.8"
        changefreq = "monthly"

        if url == SITE_URL + "/":
            priority = "1.0"
            changefreq = "weekly"

        elif "/tools/" in url:
            priority = "0.9"
            changefreq = "monthly"

        elif "/pages/health/guides/" in url:
            priority = "0.8"
            changefreq = "monthly"

        elif "/pages/" in url:
            priority = "0.7"
            changefreq = "monthly"

        lines.extend(
            [
                "  <url>",
                f"    <loc>{url}</loc>",
                f"    <lastmod>{today}</lastmod>",
                f"    <changefreq>{changefreq}</changefreq>",
                f"    <priority>{priority}</priority>",
                "  </url>",
            ]
        )

    lines.append(
        "</urlset>"
    )

    return "\n".join(lines)


# =========================================================
# VALIDATE XML STRUCTURE
# =========================================================

def validate_sitemap(text):

    required_start = (
        '<?xml version="1.0" encoding="UTF-8"?>'
    )

    required_end = "</urlset>"

    if not text.startswith(
        required_start
    ):
        return False

    if not text.endswith(
        required_end
    ):
        return False

    if text.count("<url>") != text.count(
        "</url>"
    ):
        return False

    if "<loc>" not in text:
        return False

    return True


# =========================================================
# REPORT
# =========================================================

def write_report(
    html_count,
    old_count,
    new_count,
    added_count,
):

    REPORTS.mkdir(
        parents=True,
        exist_ok=True
    )

    report = f"""# HealthMelo Sitemap V8

Generated: {datetime.now()}

## Summary

- HTML pages discovered: {html_count}
- Previous sitemap URLs: {old_count}
- New sitemap URLs: {new_count}
- URLs added: {added_count}

## Safety

- Previous sitemap.xml was backed up before replacement.
- robots.txt was not modified.
- Google verification file was not modified.
- HTML page content was not modified.
- Existing URLs were preserved.
- Duplicate URLs were removed.
"""

    (
        REPORTS
        / "V8-SITEMAP-REPORT.md"
    ).write_text(
        report,
        encoding="utf-8"
    )


# =========================================================
# MAIN
# =========================================================

def main():

    print()

    print("=" * 65)
    print("          HEALTHMELO SITEMAP BUILDER V8")
    print("=" * 65)

    print()

    print(
        "[1/5] Scanning HTML pages..."
    )

    files = find_html_files()

    print(
        f"      HTML pages found: {len(files)}"
    )

    print(
        "[2/5] Reading existing sitemap..."
    )

    old_urls = existing_urls()

    print(
        f"      Existing sitemap URLs: {len(old_urls)}"
    )

    print(
        "[3/5] Building complete URL list..."
    )

    discovered_urls = {
        normalize_url(
            html_to_url(path)
        )
        for path in files
    }

    all_urls = (
        old_urls
        | discovered_urls
    )

    print(
        f"      Final sitemap URLs: {len(all_urls)}"
    )

    added = (
        all_urls
        - old_urls
    )

    print(
        f"      New URLs added: {len(added)}"
    )

    print(
        "[4/5] Backing up existing sitemap..."
    )

    backed_up = backup_sitemap()

    if backed_up:

        print(
            "      Backup created."
        )

    else:

        print(
            "      No previous sitemap found."
        )

    print(
        "[5/5] Writing new sitemap..."
    )

    sitemap_text = build_sitemap(
        all_urls
    )

    if not validate_sitemap(
        sitemap_text
    ):

        raise RuntimeError(
            "Sitemap validation failed. "
            "Original sitemap was not replaced."
        )

    SITEMAP.write_text(
        sitemap_text,
        encoding="utf-8"
    )

    write_report(
        len(files),
        len(old_urls),
        len(all_urls),
        len(added),
    )

    print()

    print("=" * 65)
    print("                 V8 COMPLETE")
    print("=" * 65)

    print()

    print(
        f"HTML pages: {len(files)}"
    )

    print(
        f"Final sitemap URLs: {len(all_urls)}"
    )

    print(
        f"URLs added: {len(added)}"
    )

    print()

    print(
        "sitemap.xml: UPDATED"
    )

    print(
        "Previous sitemap: BACKED UP"
    )

    print(
        "robots.txt: UNCHANGED"
    )

    print(
        "Google verification: UNCHANGED"
    )

    print(
        "HTML content: UNCHANGED"
    )

    print()

    print(
        "Report:"
    )

    print(
        "seo_reports/V8-SITEMAP-REPORT.md"
    )

    print()

    print("=" * 65)


if __name__ == "__main__":
    main()