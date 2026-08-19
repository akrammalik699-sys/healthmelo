from pathlib import Path
import re, shutil, datetime, json

ROOT = Path(".")
STAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
BACKUP = ROOT / f"_backup_before_upgrade_{STAMP}"
BACKUP.mkdir(exist_ok=True)

files = [p for p in ROOT.rglob("*.html")
         if "backup" not in str(p).lower()
         and ".bad" not in str(p).lower()
         and ".bak" not in str(p).lower()]

report = []
stats = {
    "html": len(files),
    "missing_viewport": 0,
    "missing_title": 0,
    "missing_description": 0,
    "missing_canonical": 0,
    "missing_h1": 0,
    "multiple_h1": 0,
    "missing_lang": 0,
    "missing_robots": 0,
    "missing_ga": 0,
    "possible_mojibake": 0,
    "possible_markdown": 0,
    "jsonld": 0,
}

for p in files:
    s = p.read_text(encoding="utf-8", errors="replace")

    # Backup only important source files
    dest = BACKUP / p
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)

    title = re.search(r"<title[^>]*>(.*?)</title>", s, re.I | re.S)
    desc = re.search(r'<meta[^>]+name=["\']description["\']', s, re.I)
    canon = re.search(r'<link[^>]+rel=["\']canonical["\']', s, re.I)
    lang = re.search(r'<html[^>]+lang=["\']([^"\']+)', s, re.I)
    viewport = re.search(r'<meta[^>]+name=["\']viewport["\']', s, re.I)
    robots = re.search(r'<meta[^>]+name=["\']robots["\']', s, re.I)
    h1 = re.findall(r"<h1\b", s, re.I)

    issues = []

    if not viewport:
        stats["missing_viewport"] += 1
        issues.append("MOBILE_VIEWPORT")

    if not title:
        stats["missing_title"] += 1
        issues.append("TITLE")

    if not desc:
        stats["missing_description"] += 1
        issues.append("DESCRIPTION")

    if not canon:
        stats["missing_canonical"] += 1
        issues.append("CANONICAL")

    if not lang:
        stats["missing_lang"] += 1
        issues.append("LANG")

    if not robots:
        stats["missing_robots"] += 1
        issues.append("ROBOTS")

    if len(h1) == 0:
        stats["missing_h1"] += 1
        issues.append("H1")

    if len(h1) > 1:
        stats["multiple_h1"] += 1
        issues.append("MULTIPLE_H1")

    if "G-6LVMCEKWEN" not in s:
        stats["missing_ga"] += 1
        issues.append("GA")

    if "à¤" in s or "â€" in s or "ï»¿" in s:
        stats["possible_mojibake"] += 1
        issues.append("ENCODING")

    if "[https://" in s or "[http://" in s:
        stats["possible_markdown"] += 1
        issues.append("MARKDOWN_URL")

    if re.search(r'<script[^>]+type=["\']application/ld\+json["\']', s, re.I):
        stats["jsonld"] += 1

    if issues:
        report.append(f"{p} :: " + ", ".join(issues))

# sitemap
sitemap = ROOT / "sitemap.xml"
sitemap_urls = 0
if sitemap.exists():
    sitemap_urls = len(re.findall(r"<loc>\s*(.*?)\s*</loc>", sitemap.read_text(encoding="utf-8", errors="replace"), re.I))

# save report
out = ROOT / "RAPID-SEO-UPGRADE-REPORT.md"
with out.open("w", encoding="utf-8") as f:
    f.write("# HealthMelo Rapid SEO Upgrade Report\n\n")
    f.write(f"Generated: {STAMP}\n\n")
    f.write("## Project\n\n")
    f.write(f"- HTML pages: {stats['html']}\n")
    f.write(f"- Sitemap URLs: {sitemap_urls}\n")
    f.write(f"- JSON-LD pages: {stats['jsonld']}\n\n")
    f.write("## Checks\n\n")
    for k, v in stats.items():
        if k != "html":
            f.write(f"- {k}: {v}\n")
    f.write("\n## Pages needing attention\n\n")
    if report:
        for x in report:
            f.write(f"- {x}\n")
    else:
        f.write("- None detected.\n")
    f.write("\n## Backup\n\n")
    f.write(str(BACKUP) + "\n")

print("\n==============================================")
print("     HEALTHMELO RAPID SEO / MOBILE CHECK")
print("==============================================")
print("HTML pages:", stats["html"])
print("Sitemap URLs:", sitemap_urls)
print("JSON-LD pages:", stats["jsonld"])
print("----------------------------------------------")
print("Missing viewport:", stats["missing_viewport"])
print("Missing title:", stats["missing_title"])
print("Missing description:", stats["missing_description"])
print("Missing canonical:", stats["missing_canonical"])
print("Missing lang:", stats["missing_lang"])
print("Missing robots:", stats["missing_robots"])
print("Missing H1:", stats["missing_h1"])
print("Multiple H1:", stats["multiple_h1"])
print("Missing GA:", stats["missing_ga"])
print("Possible Hindi encoding:", stats["possible_mojibake"])
print("Possible Markdown URLs:", stats["possible_markdown"])
print("----------------------------------------------")
print("BACKUP:", BACKUP)
print("REPORT:", out)
print("==============================================")
print("NO WEBSITE FILES WERE MODIFIED.")
print("==============================================")
