from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(__file__).parent
BASE = "https://legendary-llama-0aca4c.netlify.app"

print("=" * 60)
print("       HEALTHMELO 2.0 SAFE UPGRADE")
print("=" * 60)

# ------------------------------------------------------------
# 1. SAFETY BACKUP
# ------------------------------------------------------------
backup = ROOT / ("_backup_hm2_safe_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

shutil.copytree(
    ROOT,
    backup,
    ignore=shutil.ignore_patterns(
        "_backup*",
        ".git",
        "__pycache__"
    )
)

print("Backup:", backup.name)

# ------------------------------------------------------------
# 2. EDITORIAL POLICY
# ------------------------------------------------------------
editorial = ROOT / "pages" / "editorial-policy" / "index.html"
editorial.parent.mkdir(parents=True, exist_ok=True)

editorial.write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>HealthMelo Editorial Policy | Health Content Standards</title>

<meta name="description"
content="Learn how HealthMelo creates, updates, sources and maintains health, nutrition and fitness information.">

<meta name="robots" content="index,follow">

<link rel="canonical"
href="{BASE}/pages/editorial-policy/">

</head>

<body>

<header>
<h1>HealthMelo Editorial Policy</h1>

<p>
HealthMelo aims to provide clear, useful and trustworthy
health, nutrition and fitness information for general education.
</p>
</header>

<main>

<section>
<h2>Our Content Principles</h2>

<p>
HealthMelo focuses on practical, understandable and
people-first health education.
</p>

<p>
Health information on this website is provided for general
educational purposes and is not a substitute for individualized
medical advice, diagnosis or treatment.
</p>
</section>

<section>
<h2>Sources and Evidence</h2>

<p>
HealthMelo aims to use reliable health and scientific sources
when developing health information.
</p>

<p>
Important health claims should be supported by appropriate
references where available.
</p>
</section>

<section>
<h2>Content Updates</h2>

<p>
Health information can change as scientific evidence and
professional recommendations evolve.
</p>

<p>
Important content may be reviewed and updated when appropriate.
</p>
</section>

<section>
<h2>Authors and Professional Review</h2>

<p>
Where author or qualified professional review information is
provided, it will be identified transparently on the relevant page.
</p>

<p>
HealthMelo does not claim medical qualifications that are not
actually held.
</p>
</section>

<section>
<h2>Medical Disclaimer</h2>

<p>
HealthMelo provides general educational information.
It does not replace diagnosis, treatment or personalized
medical advice from a qualified healthcare professional.
</p>

<p>
For urgent, severe or concerning symptoms, seek appropriate
professional medical care.
</p>
</section>

<section>
<h2>Corrections</h2>

<p>
If you find an error or have information that should be corrected,
please contact HealthMelo.
</p>

<p>
<a href="../contact/">Contact HealthMelo</a>
</p>
</section>

</main>

<footer>

<p>
<a href="../about/">About</a> |
<a href="../contact/">Contact</a> |
<a href="../privacy/">Privacy</a> |
<a href="../disclaimer/">Disclaimer</a>
</p>

</footer>

</body>
</html>
""", encoding="utf-8")

print("Created:", editorial)

# ------------------------------------------------------------
# 3. VIDEOTUBE HUB
# ------------------------------------------------------------
videos = ROOT / "pages" / "videos" / "index.html"
videos.parent.mkdir(parents=True, exist_ok=True)

videos.write_text(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>HealthMelo VideoTube | Health, Nutrition & Fitness Videos</title>

<meta name="description"
content="HealthMelo VideoTube for simple health, nutrition, fitness and calculator education videos.">

<meta name="robots" content="index,follow">

<link rel="canonical"
href="{BASE}/pages/videos/">

</head>

<body>

<header>

<h1>HealthMelo VideoTube</h1>

<p>
Simple health, nutrition and fitness videos.
</p>

</header>

<main>

<section>

<h2>HealthMelo Video Library</h2>

<p>
Welcome to HealthMelo VideoTube.
This section will contain educational videos covering
health, nutrition, fitness and HealthMelo tools.
</p>

</section>

<section>

<h2>Video Categories</h2>

<ul>
<li>Health Education</li>
<li>Nutrition</li>
<li>Fitness</li>
<li>Healthy Habits</li>
<li>Calculator Tutorials</li>
<li>Hindi Health Education</li>
</ul>

</section>

<section>

<h2>Video Quality Standard</h2>

<p>
Published videos should provide useful context and accurate
educational information. Relevant sources and related
HealthMelo resources should be provided where appropriate.
</p>

</section>

<section>

<h2>Important Information</h2>

<p>
HealthMelo videos are intended for general education and do not
replace individualized medical advice, diagnosis or treatment.
</p>

</section>

</main>

<footer>

<p>
<a href="../../index.html">HealthMelo Home</a> |
<a href="../editorial-policy/">Editorial Policy</a> |
<a href="../contact/">Contact</a>
</p>

</footer>

</body>
</html>
""", encoding="utf-8")

print("Created:", videos)

# ------------------------------------------------------------
# 4. HOMEPAGE SAFE ORGANIZATION + WEBSITE SCHEMA
# ------------------------------------------------------------
home = ROOT / "index.html"

if home.exists():

    html = home.read_text(encoding="utf-8")

    marker = "HEALTHMELO_2_0_SCHEMA"

    if marker not in html:

        schema = f"""
<!-- HEALTHMELO_2_0_SCHEMA -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "{BASE}/#organization",
      "name": "HealthMelo",
      "url": "{BASE}/"
    }},
    {{
      "@type": "WebSite",
      "@id": "{BASE}/#website",
      "name": "HealthMelo",
      "url": "{BASE}/",
      "publisher": {{
        "@id": "{BASE}/#organization"
      }}
    }}
  ]
}}
</script>
<!-- /HEALTHMELO_2_0_SCHEMA -->
"""

        if "</head>" in html.lower():

            position = html.lower().find("</head>")

            html = (
                html[:position]
                + schema
                + html[position:]
            )

            home.write_text(html, encoding="utf-8")

            print("Updated:", home)

        else:

            print("WARNING: homepage has no </head>")

    else:

        print("Homepage schema already exists.")

else:

    print("WARNING: homepage index.html not found.")

# ------------------------------------------------------------
# 5. DO NOT MODIFY EXISTING HEALTH CONTENT
# ------------------------------------------------------------
print()
print("=" * 60)
print("HEALTHMELO 2.0 FOUNDATION COMPLETE")
print("=" * 60)

print("Editorial Policy: CREATED")
print("VideoTube Hub: CREATED")
print("Homepage Organization/WebSite schema: ADDED")
print("Existing calculators: PRESERVED")
print("Existing guides: PRESERVED")
print("Existing SEO metadata: PRESERVED")
print("Fake doctor/reviewer information: NOT ADDED")
print("Fake YouTube URLs: NOT ADDED")
print()
print("NEXT: Run the SEO audit before deployment.")