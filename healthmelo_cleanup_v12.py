from pathlib import Path
import shutil
from datetime import datetime

ROOT = Path(__file__).resolve().parent
BACKUP = ROOT.parent / "HEALTH_MELO_BACKUP"

print()
print("=" * 65)
print("             HEALTHMELO CLEANUP V12")
print("=" * 65)
print()

# =========================================================
# FILES
# =========================================================

files = [
    p for p in ROOT.rglob("*.html")
    if ".git" not in p.parts
    and ".netlify" not in p.parts
    and "seo_reports" not in p.parts
    and not p.name.startswith("google")
]

print("[1/4] Scanning HTML pages...")
print("      Pages found:", len(files))

# =========================================================
# TEXT FIXES
# =========================================================

replacements = {

    # Common mojibake
    "â¤ï¸": "❤️",
    "ðŸ©º": "🩺",
    "ðŸŒ¿": "🌿",
    "ðŸ›¡ï¸": "🛡️",
    "ðŸ¥—": "🥗",
    "ðŸƒ": "🏃",
    "ðŸ§®": "🧮",
    "ðŸ“–": "📖",
    "ðŸ”¬": "🔬",
    "âš–ï¸": "⚖️",
    "âš ï¸": "⚠️",
    "â‡’": "→",

    # Hindi mojibake
    "à¤¹à¤¿à¤‚à¤¦à¥€": "हिंदी",

    # Text duplication / cleanup
    "Fitness & Fitness & Exercise": "Fitness & Exercise",
    "Health Guidess": "Health Guides",
    "Health Guidess & Common Health Questions":
        "Health Guides & Common Health Questions",

    "Calorie Calculators": "calorie calculators",
    "Calorie Calculator s": "calorie calculators",

    # Common arrow variants
    "â†’": "→",
    "â†’": "→",

    # Broken copyright
    "Â©": "©",
}

print()
print("[2/4] Cleaning encoding and duplicated text...")

changed_files = 0
replacement_count = 0

for path in files:

    try:
        original = path.read_text(
            encoding="utf-8",
            errors="replace"
        )
    except Exception:
        continue

    updated = original

    for old, new in replacements.items():

        count = updated.count(old)

        if count:
            updated = updated.replace(old, new)
            replacement_count += count

    if updated != original:

        relative = path.relative_to(ROOT)

        backup_path = BACKUP / relative

        backup_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy2(
            path,
            backup_path
        )

        path.write_text(
            updated,
            encoding="utf-8"
        )

        changed_files += 1

        print(
            "      FIXED:",
            str(relative).replace("\\", "/")
        )

# =========================================================
# REPORT
# =========================================================

print()
print("[3/4] Writing cleanup report...")

REPORT_DIR = ROOT / "seo_reports"

REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

report = f"""# HealthMelo V12 Cleanup Report

Generated: {datetime.now()}

## Summary

- HTML files scanned: {len(files)}
- Files changed: {changed_files}
- Text replacements: {replacement_count}

## Cleanup

Fixed common UTF-8 mojibake and duplicated visible text.

Examples:

- Broken emoji encoding
- Broken Hindi encoding
- Duplicate "Fitness &"
- Duplicate "Health Guides"
- Broken arrows
- Broken copyright symbol

## Safety

- Existing page structure preserved.
- Existing links were not intentionally changed.
- Existing sitemap.xml was not modified.
- Existing robots.txt was not modified.
- Google verification file was not modified.
- Modified files were backed up before changes.
"""

REPORT_DIR.joinpath(
    "V12-CLEANUP-REPORT.md"
).write_text(
    report,
    encoding="utf-8"
)

# =========================================================
# COMPLETE
# =========================================================

print()
print("[4/4] Finalizing...")

print()
print("=" * 65)
print("                 V12 COMPLETE")
print("=" * 65)
print()

print("HTML files scanned:", len(files))
print("Files changed:", changed_files)
print("Text replacements:", replacement_count)

print()
print("Sitemap: UNCHANGED")
print("Robots.txt: UNCHANGED")
print("Google verification: UNCHANGED")
print("Backups: CREATED")

print()
print("Report:")
print("seo_reports/V12-CLEANUP-REPORT.md")

print()
print("=" * 65)