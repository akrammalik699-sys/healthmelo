from pathlib import Path
from html.parser import HTMLParser
import re
from urllib.parse import urlparse
from datetime import datetime


ROOT = Path(__file__).resolve().parent


class SEOParser(HTMLParser):

    def __init__(self):
        super().__init__()

        self.title = ""
        self.description = ""
        self.canonical = ""
        self.h1_count = 0
        self.links = []

        self.in_title = False
        self.in_h1 = False

    def handle_starttag(self, tag, attrs):

        attrs = dict(attrs)

        if tag == "title":
            self.in_title = True

        if tag == "h1":
            self.h1_count += 1

        if tag == "meta":

            if attrs.get("name", "").lower() == "description":
                self.description = attrs.get("content", "")

        if tag == "link":

            if attrs.get("rel", "").lower() == "canonical":
                self.canonical = attrs.get("href", "")

        if tag == "a":

            href = attrs.get("href")

            if href:
                self.links.append(href)

    def handle_endtag(self, tag):

        if tag == "title":
            self.in_title = False

    def handle_data(self, data):

        if self.in_title:
            self.title += data


# =========================================================
# SCAN HTML
# =========================================================

html_files = [
    p for p in ROOT.rglob("*.html")
    if ".git" not in p.parts
    and ".netlify" not in p.parts
    and "seo_reports" not in p.parts
    and not p.name.startswith("google")
]


print()
print("=" * 65)
print("             HEALTHMELO FINAL SEO AUDIT")
print("=" * 65)
print()

print("[1/7] Scanning HTML pages...")

print(
    "      HTML files:",
    len(html_files)
)


# =========================================================
# SEO CHECKS
# =========================================================

missing_title = []
missing_description = []
missing_canonical = []
multiple_h1 = []
no_h1 = []

pages_data = []


print("[2/7] Checking titles, descriptions and canonicals...")


for path in html_files:

    try:

        html = path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception:

        continue


    parser = SEOParser()

    try:

        parser.feed(html)

    except Exception:

        pass


    relative = str(
        path.relative_to(ROOT)
    ).replace("\\", "/")


    if not parser.title.strip():

        missing_title.append(relative)


    if not parser.description.strip():

        missing_description.append(relative)


    if not parser.canonical.strip():

        missing_canonical.append(relative)


    if parser.h1_count == 0:

        no_h1.append(relative)


    if parser.h1_count > 1:

        multiple_h1.append(relative)


    pages_data.append(
        {
            "path": relative,
            "links": parser.links,
            "title": parser.title.strip()
        }
    )


print("[3/7] Checking internal links...")


# =========================================================
# INTERNAL LINK CHECK
# =========================================================

valid_targets = set()


for path in html_files:

    relative = str(
        path.relative_to(ROOT)
    ).replace("\\", "/")

    valid_targets.add(relative)

    if relative.endswith("/index.html"):

        valid_targets.add(
            "/" + relative[:-10]
        )

    valid_targets.add(
        "/" + relative
    )


broken_links = []


for page in pages_data:

    source = page["path"]

    for href in page["links"]:

        href = href.strip()

        if not href:
            continue

        if href.startswith("#"):
            continue

        if href.startswith(
            (
                "http://",
                "https://",
                "//",
                "mailto:",
                "tel:",
                "javascript:"
            )
        ):
            continue

        clean = href.split("#")[0]
        clean = clean.split("?")[0]

        if not clean.startswith("/"):
            continue

        clean = clean.lstrip("/")

        candidates = [
            clean,
            clean + "index.html",
            clean.rstrip("/") + "/index.html"
        ]

        if not any(
            candidate in valid_targets
            or "/" + candidate in valid_targets
            for candidate in candidates
        ):

            broken_links.append(
                (source, href)
            )


# =========================================================
# SITEMAP
# =========================================================

print("[4/7] Checking sitemap...")


sitemap_path = ROOT / "sitemap.xml"

sitemap_urls = []


if sitemap_path.exists():

    sitemap_text = sitemap_path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    sitemap_urls = re.findall(
        r"<loc>\s*(.*?)\s*</loc>",
        sitemap_text,
        flags=re.IGNORECASE
    )


else:

    sitemap_text = ""


# =========================================================
# SPECIAL FILES
# =========================================================

print("[5/7] Checking important project files...")


important_files = {

    "sitemap.xml":
        (ROOT / "sitemap.xml").exists(),

    "robots.txt":
        (ROOT / "robots.txt").exists(),

    "Google verification":
        any(
            p.name.startswith("google")
            and p.suffix == ".html"
            for p in ROOT.iterdir()
        ),

    "index.html":
        (ROOT / "index.html").exists(),

    "tools directory":
        (ROOT / "tools").exists(),

    "health guides":
        (ROOT / "pages" / "health" / "guides").exists(),

    "Hindi guides":
        (ROOT / "pages" / "hi" / "guides").exists()
}


# =========================================================
# TOOL COUNTS
# =========================================================

print("[6/7] Counting tools and content...")


tools = [
    p for p in (ROOT / "tools").glob("*/index.html")
    if p.is_file()
]


english_guides = [
    p for p in (ROOT / "pages" / "health" / "guides").glob(
        "*/index.html"
    )
    if p.is_file()
]


hindi_guides = [
    p for p in (ROOT / "pages" / "hi" / "guides").glob(
        "*/index.html"
    )
    if p.is_file()
]


# =========================================================
# FINAL STATUS
# =========================================================

errors = (
    len(missing_title)
    + len(missing_description)
    + len(missing_canonical)
    + len(multiple_h1)
    + len(broken_links)
)


status = "PASS" if errors == 0 else "REVIEW REQUIRED"


print("[7/7] Generating final report...")


REPORT_DIR = ROOT / "seo_reports"

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


report = f"""# HealthMelo Final SEO Audit

Generated: {datetime.now()}

## Overall Status

**{status}**

## Site Summary

- HTML pages: {len(html_files)}
- Sitemap URLs: {len(sitemap_urls)}
- Health tools: {len(tools)}
- English health guides: {len(english_guides)}
- Hindi health guides: {len(hindi_guides)}

## SEO Checks

### Missing Titles

Count: {len(missing_title)}

{chr(10).join("- " + x for x in missing_title) if missing_title else "- None"}

### Missing Meta Descriptions

Count: {len(missing_description)}

{chr(10).join("- " + x for x in missing_description) if missing_description else "- None"}

### Missing Canonicals

Count: {len(missing_canonical)}

{chr(10).join("- " + x for x in missing_canonical) if missing_canonical else "- None"}

### Pages With Multiple H1

Count: {len(multiple_h1)}

{chr(10).join("- " + x for x in multiple_h1) if multiple_h1 else "- None"}

### Pages Without H1

Count: {len(no_h1)}

{chr(10).join("- " + x for x in no_h1) if no_h1 else "- None"}

## Broken Internal Links

Count: {len(broken_links)}

{chr(10).join("- " + a + " -> " + b for a, b in broken_links[:100]) if broken_links else "- None"}

## Important Files

"""


for name, exists in important_files.items():

    report += (
        f"- {name}: "
        + ("OK" if exists else "MISSING")
        + "\n"
    )


report += f"""

## Tools

Total tools: {len(tools)}

"""


for tool in tools:

    relative = str(
        tool.relative_to(ROOT)
    ).replace("\\", "/")

    report += f"- {relative}\n"


report += f"""

## Health Guides

English guides: {len(english_guides)}

Hindi guides: {len(hindi_guides)}

## Sitemap

Sitemap file exists: {"YES" if sitemap_path.exists() else "NO"}

Sitemap URLs: {len(sitemap_urls)}

## Safety

- Existing page content was not modified.
- Sitemap was only read.
- Robots.txt was only read.
- Google verification was only read.
- No files were deleted.
- No existing pages were overwritten.

"""


report_path = (
    REPORT_DIR
    / "FINAL-SEO-AUDIT.md"
)


report_path.write_text(
    report,
    encoding="utf-8"
)


print()
print("=" * 65)
print("                 FINAL AUDIT COMPLETE")
print("=" * 65)
print()

print("Status:", status)

print(
    "HTML pages:",
    len(html_files)
)

print(
    "Sitemap URLs:",
    len(sitemap_urls)
)

print(
    "Tools:",
    len(tools)
)

print(
    "English guides:",
    len(english_guides)
)

print(
    "Hindi guides:",
    len(hindi_guides)
)

print()

print(
    "Missing titles:",
    len(missing_title)
)

print(
    "Missing descriptions:",
    len(missing_description)
)

print(
    "Missing canonicals:",
    len(missing_canonical)
)

print(
    "Multiple H1:",
    len(multiple_h1)
)

print(
    "Broken internal links:",
    len(broken_links)
)

print()

print(
    "Report:"
)

print(
    "seo_reports/FINAL-SEO-AUDIT.md"
)

print()

print("=" * 65)