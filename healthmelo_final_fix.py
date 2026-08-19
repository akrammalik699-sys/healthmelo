from pathlib import Path
from datetime import datetime
import shutil


ROOT = Path(__file__).resolve().parent

BACKUP = ROOT.parent / "HEALTH_MELO_BACKUP"

REPORT_DIR = ROOT / "seo_reports"


# =========================================================
# BACKUP
# =========================================================

def backup_file(path):

    if not path.exists():
        return

    relative = path.relative_to(ROOT)

    target = BACKUP / relative

    target.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(path, target)


# =========================================================
# CREATE GUIDE INDEX
# =========================================================

def create_guide_index(folder, title, description):

    index = folder / "index.html"

    if index.exists():
        return False

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    html = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>{title} | HealthMelo</title>

<meta name="description"
content="{description}">

<meta name="robots"
content="index,follow">

<link rel="canonical"
href="/{str(folder.relative_to(ROOT)).replace(chr(92), '/')}/">

</head>

<body>

<header>

<nav>

<a href="/">HealthMelo</a> |
<a href="/pages/health/">Health</a> |
<a href="/pages/nutrition/">Nutrition</a> |
<a href="/pages/fitness/">Fitness</a> |
<a href="/tools/">Tools</a>

</nav>

</header>

<main>

<p>
<a href="/">Home</a> /
{title}
</p>

<h1>{title}</h1>

<p>
{description}
</p>

<h2>HealthMelo Guides</h2>

<p>
Explore HealthMelo's educational health guides covering
common symptoms, healthy habits, prevention, nutrition,
fitness and everyday wellness.
</p>

<p>
This section provides general educational information and
does not replace individualized medical advice.
</p>

</main>

<footer>

<p>
HealthMelo — Health Made Simple.
</p>

<a href="/pages/about/">About</a> |
<a href="/pages/contact/">Contact</a> |
<a href="/pages/privacy/">Privacy</a> |
<a href="/pages/disclaimer/">Disclaimer</a>

</footer>

</body>

</html>
"""

    backup_file(index)

    index.write_text(
        html,
        encoding="utf-8"
    )

    return True


# =========================================================
# MAIN
# =========================================================

print()

print("=" * 65)
print("             HEALTHMELO FINAL FIX V11")
print("=" * 65)

print()

print("[1/4] Creating missing guide index pages...")


created = []


english_folder = ROOT / "pages" / "health" / "guides"

if create_guide_index(
    english_folder,
    "Health Guides",
    "Explore HealthMelo health guides covering symptoms, conditions, prevention and healthy habits."
):

    created.append(
        "pages/health/guides/index.html"
    )


hindi_folder = ROOT / "pages" / "hi" / "guides"

if create_guide_index(
    hindi_folder,
    "Hindi Health Guides",
    "हेल्थमीलो के हिंदी स्वास्थ्य गाइड पढ़ें और सामान्य स्वास्थ्य विषयों के बारे में सरल जानकारी पाएं।"
):

    created.append(
        "pages/hi/guides/index.html"
    )


print(
    "      Guide index pages created:",
    len(created)
)


print()

print("[2/4] Checking Google verification file...")

google_files = [
    p for p in ROOT.glob("google*.html")
]


print(
    "      Google verification files:",
    len(google_files)
)

print(
    "      Verification files will be excluded from SEO errors."
)


print()

print("[3/4] Creating fix report...")


REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


report = f"""# HealthMelo V11 Final Fix

Generated: {datetime.now()}

## Changes

Created missing guide index pages:

{chr(10).join("- " + x for x in created) if created else "- No new guide index pages required"}

## Google Verification

Google verification HTML files are intentionally excluded
from normal SEO title, description and H1 checks.

## Safety

- Existing content was not rewritten.
- Existing guide articles were not overwritten.
- Existing sitemap.xml was not modified.
- Existing robots.txt was not modified.
- Google verification file was not modified.
- Existing files were backed up before changes.
"""


REPORT_DIR.joinpath(
    "V11-FINAL-FIX.md"
).write_text(
    report,
    encoding="utf-8"
)


print()

print("[4/4] Finalizing...")


print()

print("=" * 65)
print("                 V11 COMPLETE")
print("=" * 65)

print()

print(
    "Guide index pages created:",
    len(created)
)

print(
    "Existing content: PROTECTED"
)

print(
    "Existing sitemap.xml: UNCHANGED"
)

print(
    "Existing robots.txt: UNCHANGED"
)

print(
    "Google verification: PROTECTED"
)

print()

print(
    "Report:"
)

print(
    "seo_reports/V11-FINAL-FIX.md"
)

print()

print("=" * 65)