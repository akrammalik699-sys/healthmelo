from pathlib import Path
from datetime import datetime
import json
import shutil


ROOT = Path(__file__).resolve().parent
REPORTS = ROOT / "seo_reports"
BACKUP = ROOT.parent / "HEALTH_MELO_BACKUP"

SITE_URL = "https://legendary-llama-0aca4c.netlify.app"


ARTICLES = [

    {
        "slug": "healthy-eating-basics",
        "title": "Healthy Eating Basics: A Simple Guide to Balanced Nutrition",
        "description": "Learn the basics of balanced eating, nutritious foods, portion awareness and practical healthy eating habits.",
        "category": "Nutrition",
        "intro": "Healthy eating does not require a complicated diet. A balanced eating pattern can include a variety of vegetables, fruits, whole grains, protein foods and healthy fats.",
        "sections": [
            (
                "What Does Healthy Eating Mean?",
                "Healthy eating means choosing a variety of foods that provide the nutrients your body needs. The goal is not perfection but a balanced pattern that can be followed consistently."
            ),
            (
                "Build a Balanced Plate",
                "A practical approach is to include vegetables or fruit, a source of protein, a whole-grain or other carbohydrate source, and a moderate amount of healthy fat. The exact amounts can vary according to individual needs."
            ),
            (
                "Choose Nutrient-Dense Foods",
                "Foods such as vegetables, fruits, legumes, whole grains, nuts, seeds, eggs, dairy products and other protein-rich foods can provide useful nutrients. Minimally processed foods can be a helpful foundation."
            ),
            (
                "Healthy Eating Habits",
                "Plan meals when possible, drink water regularly, pay attention to hunger and fullness, and avoid relying heavily on highly processed foods and sugary drinks."
            ),
            (
                "When to Seek Individual Advice",
                "People with medical conditions, food allergies, pregnancy-related nutritional needs or other special dietary requirements may need individualized advice from a qualified healthcare professional or registered dietitian."
            )
        ]
    },

    {
        "slug": "daily-hydration-guide",
        "title": "Daily Hydration Guide: How to Stay Hydrated",
        "description": "Learn practical hydration habits, signs of dehydration and simple ways to support healthy fluid intake.",
        "category": "Health",
        "intro": "Water is important for many normal body functions. Hydration needs vary between people and can change with activity, weather, diet and health conditions.",
        "sections": [
            (
                "Why Hydration Matters",
                "Fluids help support normal circulation, temperature regulation, digestion and other body processes. Water is a major source of daily fluid intake."
            ),
            (
                "Signs You May Need More Fluids",
                "Thirst, a dry mouth, darker urine and reduced urination can occur when fluid intake is insufficient. These signs are not always specific, so they should be considered along with the overall situation."
            ),
            (
                "Simple Hydration Habits",
                "Keep water available during the day, drink with meals, and increase attention to fluids during hot weather or physical activity."
            ),
            (
                "Exercise and Hydration",
                "Long or intense exercise and hot environments can increase fluid losses. Individual needs depend on duration, intensity, temperature and sweating."
            ),
            (
                "When to Get Medical Help",
                "Severe weakness, confusion, fainting, inability to keep fluids down or other concerning symptoms require prompt medical attention."
            )
        ]
    },

    {
        "slug": "sleep-hygiene-guide",
        "title": "Sleep Hygiene: Simple Habits for Better Sleep",
        "description": "Learn practical sleep hygiene habits that can support a more consistent and restful sleep routine.",
        "category": "Health",
        "intro": "Good sleep supports physical health, mood, attention and daily functioning. Sleep hygiene refers to habits and environmental factors that can support healthy sleep.",
        "sections": [
            (
                "Keep a Consistent Schedule",
                "Going to bed and waking up at roughly consistent times can help establish a regular sleep routine."
            ),
            (
                "Create a Relaxing Evening Routine",
                "A calm routine before bed can help you transition away from daytime activities. Reading, gentle relaxation or another quiet activity may be useful."
            ),
            (
                "Make the Bedroom Sleep-Friendly",
                "A comfortable, quiet and appropriately dark environment can support sleep. Temperature and bedding preferences vary from person to person."
            ),
            (
                "Watch Caffeine and Late-Day Stimulation",
                "Caffeine can affect sleep for some people, especially when consumed later in the day. Heavy meals and stimulating activities close to bedtime may also make sleep harder for some people."
            ),
            (
                "Persistent Sleep Problems",
                "If sleep difficulties are frequent, severe or affecting daytime functioning, consider discussing them with a healthcare professional."
            )
        ]
    },

    {
        "slug": "stress-management-guide",
        "title": "Stress Management: Practical Ways to Cope With Everyday Stress",
        "description": "Learn simple, healthy strategies for managing everyday stress and supporting emotional wellbeing.",
        "category": "Health",
        "intro": "Stress is a normal response to challenging situations. Healthy coping strategies can help people manage everyday stress and maintain routines that support wellbeing.",
        "sections": [
            (
                "Understand Your Stress Triggers",
                "Identifying situations, routines or pressures that repeatedly increase stress can help you think about practical changes."
            ),
            (
                "Use Simple Relaxation Strategies",
                "Slow breathing, brief walks, stretching, quiet time and other calming activities may help reduce immediate tension."
            ),
            (
                "Stay Connected",
                "Talking with trusted family members, friends or other supportive people can provide emotional support during difficult periods."
            ),
            (
                "Support Your Basic Health",
                "Regular sleep, nutritious meals, physical activity and reasonable routines can support overall resilience."
            ),
            (
                "When to Seek Professional Support",
                "If stress feels overwhelming, persists for a long time or significantly interferes with daily life, consider speaking with a qualified mental health or healthcare professional."
            )
        ]
    },

    {
        "slug": "constipation-prevention-guide",
        "title": "Constipation Prevention: Food, Fluids and Healthy Habits",
        "description": "Learn practical habits that may help support regular bowel movements and reduce constipation risk.",
        "category": "Health",
        "intro": "Constipation can involve infrequent bowel movements, hard stools or difficulty passing stool. Habits involving food, fluids and movement can support regular bowel function.",
        "sections": [
            (
                "Eat Enough Fiber",
                "Fiber-rich foods include vegetables, fruits, legumes and whole grains. Increase fiber gradually and drink adequate fluids."
            ),
            (
                "Stay Active",
                "Regular physical activity can support normal bowel function. Even regular walking may be a useful part of an active routine."
            ),
            (
                "Respond to the Urge",
                "Ignoring the urge to have a bowel movement repeatedly may contribute to bowel difficulties for some people. Allowing enough unhurried bathroom time can help."
            ),
            (
                "Review Your Routine",
                "Changes in diet, activity, travel, stress and some medicines can affect bowel habits."
            ),
            (
                "When to Seek Care",
                "Severe abdominal pain, vomiting, blood in the stool, unexplained weight loss or persistent constipation should be discussed with a healthcare professional."
            )
        ]
    },

    {
        "slug": "common-cold-self-care",
        "title": "Common Cold Self-Care: What Can Help You Feel Better",
        "description": "Learn practical self-care measures for common cold symptoms and signs that may require medical attention.",
        "category": "Health",
        "intro": "The common cold is a viral respiratory infection. Most cases improve with time and supportive care, although symptoms can sometimes be uncomfortable.",
        "sections": [
            (
                "Rest and Fluids",
                "Getting enough rest and drinking fluids can support recovery and help prevent dehydration."
            ),
            (
                "Sore Throat and Congestion",
                "Warm fluids, saline nasal measures and other appropriate comfort measures may help relieve some symptoms."
            ),
            (
                "Cough",
                "A cough can be part of a cold and may take time to settle. Avoiding smoke and other respiratory irritants can be helpful."
            ),
            (
                "Prevent Spread",
                "Hand hygiene, covering coughs and sneezes, and staying home when unwell can reduce the spread of respiratory infections."
            ),
            (
                "When to Seek Medical Advice",
                "Breathing difficulty, severe dehydration, persistent or worsening symptoms, or other concerning symptoms should be evaluated by a healthcare professional."
            )
        ]
    },

    {
        "slug": "fever-guide",
        "title": "Fever Guide: What It Means and What to Watch For",
        "description": "Learn what fever can mean, practical supportive care and warning signs that need medical attention.",
        "category": "Health",
        "intro": "Fever is an increase in body temperature that can occur with infections and other conditions. The cause and accompanying symptoms are important when deciding what to do.",
        "sections": [
            (
                "What Is Fever?",
                "Fever is a rise in body temperature above the normal range. It is commonly associated with the body's response to infection."
            ),
            (
                "Supportive Care",
                "Rest, comfortable clothing and appropriate fluid intake can support someone who has a fever. Food intake can be guided by appetite."
            ),
            (
                "Monitor the Overall Condition",
                "Temperature is only one part of the picture. Pay attention to breathing, alertness, hydration and other symptoms."
            ),
            (
                "Children and Older Adults",
                "Age, underlying health conditions and the overall clinical picture can affect how fever should be assessed."
            ),
            (
                "Warning Signs",
                "Difficulty breathing, confusion, severe weakness, seizures, severe dehydration or other serious symptoms require prompt medical assessment."
            )
        ]
    },

    {
        "slug": "headache-self-care-guide",
        "title": "Headache Self-Care Guide: Common Triggers and Helpful Habits",
        "description": "Learn about common headache triggers, simple self-care measures and warning signs that need medical attention.",
        "category": "Health",
        "intro": "Headaches are common and can have many possible causes. Recognizing patterns and maintaining healthy routines may help with some recurring headaches.",
        "sections": [
            (
                "Common Triggers",
                "Dehydration, lack of sleep, skipped meals, stress, prolonged screen use and certain individual triggers can contribute to headaches."
            ),
            (
                "Supportive Habits",
                "Regular meals, adequate fluids, sufficient sleep and breaks from prolonged screen use may help some people."
            ),
            (
                "Track Your Headaches",
                "Recording when headaches occur, possible triggers, duration and associated symptoms can help identify patterns."
            ),
            (
                "Avoid Overusing Pain Medicines",
                "Frequent use of some headache medicines can contribute to medication-overuse headaches. Follow product instructions and seek professional advice when headaches recur frequently."
            ),
            (
                "Emergency Warning Signs",
                "A sudden extremely severe headache, headache after a serious injury, new neurological symptoms, confusion, fainting or other severe symptoms require urgent medical assessment."
            )
        ]
    },

    {
        "slug": "healthy-weight-basics",
        "title": "Healthy Weight Basics: Understanding BMI, Calories and Habits",
        "description": "Learn how BMI, calorie needs, activity and everyday habits relate to healthy weight management.",
        "category": "Nutrition",
        "intro": "Healthy weight is influenced by many factors, including nutrition, activity, sleep, genetics, medications and health conditions. No single number defines health.",
        "sections": [
            (
                "What Is BMI?",
                "Body mass index, or BMI, is a screening measure based on height and weight. It can be useful for population-level assessment but does not directly measure body fat or overall health."
            ),
            (
                "Calories and Energy Balance",
                "The body uses energy for basic functions and physical activity. Food provides energy, but individual calorie needs vary considerably."
            ),
            (
                "Focus on Sustainable Habits",
                "Balanced meals, regular movement, adequate sleep and realistic routines are generally more sustainable than extreme short-term diets."
            ),
            (
                "Use Health Tools Carefully",
                "Calculators can provide estimates and educational information. They should not be treated as a diagnosis or a personalized medical prescription."
            ),
            (
                "When to Get Professional Guidance",
                "People with significant unintentional weight changes, eating difficulties, chronic conditions or other health concerns should consider individualized professional guidance."
            )
        ]
    },

    {
        "slug": "healthy-exercise-basics",
        "title": "Exercise Basics: Cardio, Strength and Everyday Movement",
        "description": "Learn the basics of cardio, strength training, flexibility and everyday physical activity.",
        "category": "Fitness",
        "intro": "Regular physical activity can support cardiovascular health, strength, mobility, mood and overall wellbeing. A good routine can include different types of movement.",
        "sections": [
            (
                "Cardio Exercise",
                "Walking, cycling, swimming and other activities that raise the heart rate can contribute to cardiovascular fitness."
            ),
            (
                "Strength Training",
                "Resistance exercises can help maintain or improve muscle strength. Beginners can start with manageable resistance and focus on safe technique."
            ),
            (
                "Flexibility and Mobility",
                "Gentle stretching and mobility exercises can help maintain comfortable movement. Avoid forcing a painful range of motion."
            ),
            (
                "Start Gradually",
                "If you have been inactive, gradually increasing duration and intensity can be more practical than suddenly doing very demanding workouts."
            ),
            (
                "Safety First",
                "Stop activity if you experience severe pain, fainting, significant breathing difficulty or other concerning symptoms. People with certain health conditions may need professional advice before starting a new exercise program."
            )
        ]
    }

]


def esc(text):
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )


def make_article(article):

    sections_html = ""

    for heading, text in article["sections"]:

        sections_html += f"""
<section>
<h2>{esc(heading)}</h2>
<p>{esc(text)}</p>
</section>
"""

    slug = article["slug"]

    related = f"""
<section>
<h2>Related HealthMelo Tools</h2>
<p>
<a href="/tools/">Health Tools</a> |
<a href="/tools/bmi/">BMI Calculator</a> |
<a href="/tools/calorie/">Calorie Calculator</a> |
<a href="/tools/water/">Water Intake Calculator</a>
</p>
</section>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>{esc(article["title"])} | HealthMelo</title>

<meta name="description"
content="{esc(article["description"])}">

<meta name="robots"
content="index,follow">

<link rel="canonical"
href="{SITE_URL}/pages/health/guides/{slug}/">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(article["title"])},
  "description": {json.dumps(article["description"])},
  "url": {json.dumps(SITE_URL + "/pages/health/guides/" + slug + "/")},
  "publisher": {{
    "@type": "Organization",
    "name": "HealthMelo",
    "url": {json.dumps(SITE_URL + "/")}
  }}
}}
</script>

</head>

<body>

<header>

<nav>
<a href="/">HealthMelo</a> |
<a href="/pages/health/">Health</a> |
<a href="/pages/nutrition/">Nutrition</a> |
<a href="/pages/fitness/">Fitness</a> |
<a href="/tools/">Health Tools</a>
</nav>

</header>

<main>

<article>

<p>
<a href="/">Home</a> /
<a href="/pages/health/">Health</a> /
<a href="/pages/health/guides/">Guides</a>
</p>

<h1>{esc(article["title"])}</h1>

<p>{esc(article["intro"])}</p>

{sections_html}

{related}

<section>

<h2>Important Health Information</h2>

<p>
HealthMelo provides general educational information.
It is not a substitute for diagnosis, treatment or
individual medical advice. For personal health concerns,
consult a qualified healthcare professional.
</p>

</section>

</article>

</main>

<footer>

<p>
<strong>HealthMelo</strong> — Health Made Simple.
</p>

<p>
<a href="/pages/about/">About</a> |
<a href="/pages/contact/">Contact</a> |
<a href="/pages/privacy/">Privacy</a> |
<a href="/pages/disclaimer/">Disclaimer</a>
</p>

</footer>

</body>
</html>
"""

    return html


def main():

    print()
    print("=" * 65)
    print("          HEALTHMELO MASTER UPGRADE V7")
    print("=" * 65)
    print()

    print("[1/4] Preparing content expansion...")

    target = ROOT / "pages" / "health" / "guides"

    target.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"      New article opportunities: {len(ARTICLES)}"
    )

    print("[2/4] Creating new Health articles...")

    created = []

    for article in ARTICLES:

        folder = target / article["slug"]

        file = folder / "index.html"

        if file.exists():

            print(
                f"      SKIPPED existing: {article['slug']}"
            )

            continue

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            make_article(article),
            encoding="utf-8"
        )

        created.append(
            article["slug"]
        )

    print(
        f"      Articles created: {len(created)}"
    )

    print("[3/4] Creating content inventory...")

    inventory = []

    for article in ARTICLES:

        inventory.append(
            {
                "slug": article["slug"],
                "title": article["title"],
                "category": article["category"],
                "url": (
                    SITE_URL
                    + "/pages/health/guides/"
                    + article["slug"]
                    + "/"
                )
            }
        )

    REPORTS.mkdir(
        parents=True,
        exist_ok=True
    )

    (
        REPORTS / "v7-content-inventory.json"
    ).write_text(
        json.dumps(
            inventory,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    print("[4/4] Writing report...")

    report = [
        "# HealthMelo V7 Content Expansion",
        "",
        f"Generated: {datetime.now()}",
        "",
        f"- Planned articles: {len(ARTICLES)}",
        f"- New articles created: {len(created)}",
        "",
        "## New Articles",
        ""
    ]

    for article in ARTICLES:

        status = (
            "CREATED"
            if article["slug"] in created
            else "EXISTING / SKIPPED"
        )

        report.append(
            f"- **{article['title']}** — {status}"
        )

    report.extend(
        [
            "",
            "## Safety",
            "",
            "- Existing pages were not overwritten.",
            "- Existing content was not deleted.",
            "- Existing sitemap.xml was not modified.",
            "- Existing robots.txt was not modified.",
            "- Google verification file was not modified.",
            "- New articles contain general educational information.",
            "- Medical disclaimer included.",
        ]
    )

    (
        REPORTS / "V7-CONTENT-EXPANSION.md"
    ).write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print()
    print("=" * 65)
    print("                 V7 COMPLETE")
    print("=" * 65)
    print()

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
        f"New articles: {len(created)}"
    )

    print()
    print(
        "Report:"
    )

    print(
        "seo_reports/V7-CONTENT-EXPANSION.md"
    )

    print()
    print("=" * 65)


if __name__ == "__main__":
    main()