from pathlib import Path
import re, shutil, datetime

ROOT = Path(".")
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup = ROOT / f"_backup_growth_{stamp}"
backup.mkdir(exist_ok=True)

files = [
    p for p in ROOT.rglob("*.html")
    if "_backup" not in str(p)
    and not p.name.endswith((".backup",".bad",".encoding-backup"))
    and p.name != "google6dac5feead5d9a65.html"
]

for p in files:
    rel = p.relative_to(ROOT)
    dest = backup / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)

    s = p.read_text(encoding="utf-8", errors="ignore")

    # Mobile
    if 'name="viewport"' not in s.lower():
        s = s.replace(
            "<head>",
            '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1">'
        )

    # Robots
    if not re.search(r'<meta[^>]+name=["\']robots["\']', s, re.I):
        s = s.replace(
            "</head>",
            '<meta name="robots" content="index,follow,max-image-preview:large">\n</head>'
        )

    # Theme / mobile rendering
    if 'meta name="theme-color"' not in s.lower():
        s = s.replace(
            "</head>",
            '<meta name="theme-color" content="#0f766e">\n</head>'
        )

    # Improve image loading
    s = re.sub(
        r'<img(?![^>]*\bloading=)',
        '<img loading="lazy"',
        s,
        flags=re.I
    )

    # Skip duplicate enhancement
    if "HealthMelo SEO Topic Cluster" not in s:
        path = str(p).replace("\\","/")

        if "/pages/health/guides/" in path:
            cluster = """
<section class="healthmelo-topic-cluster" aria-label="Related Health Topics">
<h2>Related Health Topics</h2>
<p>Explore related HealthMelo guides for symptoms, causes, prevention, healthy habits and everyday health information.</p>
<nav>
<a href="/pages/health/guides/">Health Guides</a> |
<a href="/pages/health/">Health Information</a> |
<a href="/pages/nutrition/">Nutrition</a> |
<a href="/pages/fitness/">Fitness & Exercise</a> |
<a href="/pages/tools/">Free Health Calculators</a>
</nav>
</section>
<!-- HealthMelo SEO Topic Cluster -->
"""
            s = s.replace("</main>", cluster + "\n</main>", 1)

        elif "/pages/hi/guides/" in path:
            cluster = """
<section class="healthmelo-topic-cluster" aria-label="संबंधित स्वास्थ्य विषय">
<h2>संबंधित स्वास्थ्य जानकारी</h2>
<p>HealthMelo पर स्वास्थ्य, पोषण, फिटनेस, लक्षण और रोज़मर्रा की सेहत से जुड़ी आसान जानकारी पढ़ें।</p>
<nav>
<a href="/pages/hi/guides/">सभी हिंदी स्वास्थ्य गाइड</a> |
<a href="/pages/hi/">हिंदी स्वास्थ्य जानकारी</a> |
<a href="/pages/nutrition/">Nutrition</a> |
<a href="/pages/fitness/">Fitness</a> |
<a href="/pages/tools/">Health Calculators</a>
</nav>
</section>
<!-- HealthMelo SEO Topic Cluster -->
"""
            s = s.replace("</main>", cluster + "\n</main>", 1)

        elif "/tools/" in path:
            cluster = """
<section class="healthmelo-topic-cluster" aria-label="Related Health Calculators">
<h2>More Free Health Calculators</h2>
<p>Use HealthMelo's free calculators to understand BMI, calories, BMR, TDEE, protein, water intake, body fat and other health metrics.</p>
<nav>
<a href="/tools/bmi/">BMI Calculator</a> |
<a href="/tools/calorie/">Calorie Calculator</a> |
<a href="/tools/bmr/">BMR Calculator</a> |
<a href="/tools/tdee/">TDEE Calculator</a> |
<a href="/tools/protein/">Protein Calculator</a> |
<a href="/tools/water/">Water Intake Calculator</a>
</nav>
</section>
<!-- HealthMelo SEO Topic Cluster -->
"""
            s = s.replace("</main>", cluster + "\n</main>", 1)

    p.write_text(s, encoding="utf-8")

print("="*60)
print("HEALTHMELO RAPID GROWTH SEO UPGRADE")
print("="*60)
print("Modified pages:", len(files))
print("Backup:", backup)
print("Added: mobile + robots + theme + lazy images + topic clusters")
print("No pages deleted.")
print()
print("NEXT: python healthmelo_final_audit.py")
