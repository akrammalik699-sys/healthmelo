from pathlib import Path
from datetime import datetime
import json
import shutil


ROOT = Path(__file__).resolve().parent

SITE_URL = "https://legendary-llama-0aca4c.netlify.app"

TOOLS_DIR = ROOT / "tools"
REPORT_DIR = ROOT / "seo_reports"
BACKUP_DIR = ROOT.parent / "HEALTH_MELO_BACKUP"


# =========================================================
# TOOL DATA
# =========================================================

TOOLS = [

    {
        "slug": "protein",
        "name": "Protein Calculator",
        "title": "Protein Calculator - Daily Protein Needs | HealthMelo",
        "description": "Calculate estimated daily protein needs based on body weight, activity level and fitness goals.",
        "formula": "Protein needs are estimated using body weight and selected activity or fitness goal.",
        "intro": "Use this free protein calculator to estimate your daily protein needs based on body weight, activity level and fitness goal."
    },

    {
        "slug": "macro",
        "name": "Macro Calculator",
        "title": "Macro Calculator - Protein, Carbs & Fat | HealthMelo",
        "description": "Estimate daily calories and macronutrient targets for protein, carbohydrates and fat.",
        "formula": "Macros are estimated from daily calorie needs and selected macro percentages.",
        "intro": "Use this macro calculator to estimate daily protein, carbohydrate and fat targets."
    },

    {
        "slug": "tdee",
        "name": "TDEE Calculator",
        "title": "TDEE Calculator - Total Daily Energy Expenditure | HealthMelo",
        "description": "Estimate your Total Daily Energy Expenditure using age, sex, height, weight and activity level.",
        "formula": "TDEE is estimated by multiplying BMR by an activity factor.",
        "intro": "Use this TDEE calculator to estimate how many calories you may burn in a typical day."
    },

    {
        "slug": "body-fat",
        "name": "Body Fat Calculator",
        "title": "Body Fat Calculator - Estimate Body Fat Percentage | HealthMelo",
        "description": "Estimate body fat percentage using basic body measurements.",
        "formula": "Body fat percentage is an estimate and can vary depending on the measurement method.",
        "intro": "Use this body fat calculator to get an educational estimate of body fat percentage."
    },

    {
        "slug": "pace",
        "name": "Pace Calculator",
        "title": "Pace Calculator - Running & Walking Pace | HealthMelo",
        "description": "Calculate running or walking pace from distance and time.",
        "formula": "Pace = total time ÷ distance.",
        "intro": "Use this pace calculator to estimate your running or walking pace from distance and time."
    },

    {
        "slug": "steps-calories",
        "name": "Steps to Calories Calculator",
        "title": "Steps to Calories Calculator | HealthMelo",
        "description": "Estimate calories burned from walking steps using steps, body weight and walking intensity.",
        "formula": "Calories burned are estimated from steps, body weight and activity assumptions.",
        "intro": "Estimate calories burned from walking based on your number of steps and body weight."
    },

    {
        "slug": "heart-rate",
        "name": "Heart Rate Calculator",
        "title": "Heart Rate Calculator - Target Heart Rate Zones | HealthMelo",
        "description": "Calculate estimated maximum heart rate and exercise heart rate zones.",
        "formula": "Maximum heart rate is an estimate and individual values can vary.",
        "intro": "Use this heart rate calculator to estimate maximum heart rate and common exercise intensity zones."
    }

]


# =========================================================
# COMMON CSS
# =========================================================

CSS = """
<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: #f6f8fb;
    color: #172033;
    line-height: 1.6;
}

header {
    background: white;
    border-bottom: 1px solid #e5e7eb;
    padding: 18px 20px;
}

nav {
    max-width: 1100px;
    margin: auto;
}

nav a {
    text-decoration: none;
    margin-right: 16px;
    color: #2563eb;
    font-weight: 600;
}

main {
    max-width: 1000px;
    margin: 40px auto;
    padding: 20px;
}

.card {
    background: white;
    padding: 28px;
    border-radius: 16px;
    box-shadow: 0 5px 25px rgba(0,0,0,.06);
    margin-bottom: 25px;
}

h1 {
    font-size: 34px;
    margin-bottom: 10px;
}

h2 {
    margin-top: 28px;
}

label {
    display: block;
    font-weight: 600;
    margin-top: 15px;
}

input,
select,
button {
    width: 100%;
    padding: 13px;
    margin-top: 7px;
    border-radius: 8px;
    border: 1px solid #d1d5db;
    font-size: 16px;
}

button {
    margin-top: 22px;
    cursor: pointer;
    background: #2563eb;
    color: white;
    border: none;
    font-weight: 700;
}

button:hover {
    opacity: .9;
}

.result {
    margin-top: 20px;
    padding: 18px;
    background: #eef6ff;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 700;
}

.note {
    background: #fff8e6;
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}

footer {
    text-align: center;
    padding: 30px;
    background: white;
    margin-top: 50px;
}

</style>
"""


# =========================================================
# JAVASCRIPT CALCULATORS
# =========================================================

JS = {

"protein": """
function calculate() {

    const weight = Number(document.getElementById("weight").value);
    const activity = document.getElementById("activity").value;

    if (!weight || weight <= 0) {
        alert("Please enter a valid body weight.");
        return;
    }

    let factor = 0.8;

    if (activity === "active") {
        factor = 1.2;
    }

    if (activity === "training") {
        factor = 1.6;
    }

    if (activity === "athlete") {
        factor = 2.0;
    }

    const protein = weight * factor;

    document.getElementById("result").innerHTML =
        "Estimated daily protein: " +
        protein.toFixed(0) +
        " g/day";
}
""",


"macro": """
function calculate() {

    const calories = Number(document.getElementById("calories").value);

    if (!calories || calories <= 0) {
        alert("Please enter daily calories.");
        return;
    }

    const proteinPercent = 0.30;
    const carbPercent = 0.40;
    const fatPercent = 0.30;

    const proteinCalories = calories * proteinPercent;
    const carbCalories = calories * carbPercent;
    const fatCalories = calories * fatPercent;

    const protein = proteinCalories / 4;
    const carbs = carbCalories / 4;
    const fat = fatCalories / 9;

    document.getElementById("result").innerHTML =
        "Protein: " + protein.toFixed(0) + " g<br>" +
        "Carbohydrates: " + carbs.toFixed(0) + " g<br>" +
        "Fat: " + fat.toFixed(0) + " g";
}
""",


"tdee": """
function calculate() {

    const age = Number(document.getElementById("age").value);
    const weight = Number(document.getElementById("weight").value);
    const height = Number(document.getElementById("height").value);
    const sex = document.getElementById("sex").value;
    const activity = Number(document.getElementById("activity").value);

    if (!age || !weight || !height) {
        alert("Please complete all fields.");
        return;
    }

    let bmr;

    if (sex === "male") {
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5;
    } else {
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161;
    }

    const tdee = bmr * activity;

    document.getElementById("result").innerHTML =
        "Estimated BMR: " + bmr.toFixed(0) + " kcal/day<br>" +
        "Estimated TDEE: " + tdee.toFixed(0) + " kcal/day";
}
""",


"body-fat": """
function calculate() {

    const gender = document.getElementById("gender").value;
    const bmi = Number(document.getElementById("bmi").value);
    const age = Number(document.getElementById("age").value);

    if (!bmi || !age) {
        alert("Please enter BMI and age.");
        return;
    }

    let bodyFat;

    if (gender === "male") {
        bodyFat = (1.20 * bmi) + (0.23 * age) - 16.2;
    } else {
        bodyFat = (1.20 * bmi) + (0.23 * age) - 5.4;
    }

    if (bodyFat < 0) {
        bodyFat = 0;
    }

    document.getElementById("result").innerHTML =
        "Estimated body fat: " +
        bodyFat.toFixed(1) +
        "%";
}
""",


"pace": """
function calculate() {

    const distance = Number(document.getElementById("distance").value);
    const minutes = Number(document.getElementById("minutes").value);
    const seconds = Number(document.getElementById("seconds").value);

    if (!distance || distance <= 0) {
        alert("Please enter a valid distance.");
        return;
    }

    const totalSeconds =
        (minutes * 60) + seconds;

    const paceSeconds =
        totalSeconds / distance;

    const paceMinutes =
        Math.floor(paceSeconds / 60);

    const paceRemaining =
        Math.round(paceSeconds % 60);

    document.getElementById("result").innerHTML =
        "Pace: " +
        paceMinutes +
        ":" +
        String(paceRemaining).padStart(2, "0") +
        " min/km";
}
""",


"steps-calories": """
function calculate() {

    const steps = Number(document.getElementById("steps").value);
    const weight = Number(document.getElementById("weight").value);

    if (!steps || !weight) {
        alert("Please enter steps and body weight.");
        return;
    }

    const distanceKm =
        steps * 0.00075;

    const calories =
        distanceKm * weight * 0.5;

    document.getElementById("result").innerHTML =
        "Estimated distance: " +
        distanceKm.toFixed(2) +
        " km<br>" +
        "Estimated calories burned: " +
        calories.toFixed(0) +
        " kcal";
}
""",


"heart-rate": """
function calculate() {

    const age = Number(document.getElementById("age").value);

    if (!age || age <= 0) {
        alert("Please enter a valid age.");
        return;
    }

    const maxHR = 220 - age;

    const moderateLow = maxHR * 0.50;
    const moderateHigh = maxHR * 0.70;

    const vigorousLow = maxHR * 0.70;
    const vigorousHigh = maxHR * 0.85;

    document.getElementById("result").innerHTML =
        "Estimated maximum heart rate: " +
        maxHR.toFixed(0) +
        " bpm<br><br>" +

        "Moderate zone: " +
        moderateLow.toFixed(0) +
        "–" +
        moderateHigh.toFixed(0) +
        " bpm<br>" +

        "Vigorous zone: " +
        vigorousLow.toFixed(0) +
        "–" +
        vigorousHigh.toFixed(0) +
        " bpm";
}
"""

}


# =========================================================
# TOOL FORMS
# =========================================================

FORMS = {

"protein": """
<label>Body Weight (kg)</label>
<input id="weight" type="number" min="1" placeholder="Example: 70">

<label>Activity Level</label>
<select id="activity">
<option value="sedentary">General health</option>
<option value="active">Active</option>
<option value="training">Regular strength training</option>
<option value="athlete">High training load</option>
</select>

<button onclick="calculate()">Calculate Protein</button>
""",


"macro": """
<label>Daily Calories</label>
<input id="calories" type="number" min="500" placeholder="Example: 2000">

<button onclick="calculate()">Calculate Macros</button>
""",


"tdee": """
<label>Age</label>
<input id="age" type="number" min="1">

<label>Sex</label>
<select id="sex">
<option value="male">Male</option>
<option value="female">Female</option>
</select>

<label>Height (cm)</label>
<input id="height" type="number" min="50">

<label>Weight (kg)</label>
<input id="weight" type="number" min="10">

<label>Activity Level</label>
<select id="activity">
<option value="1.2">Sedentary</option>
<option value="1.375">Lightly active</option>
<option value="1.55">Moderately active</option>
<option value="1.725">Very active</option>
<option value="1.9">Extra active</option>
</select>

<button onclick="calculate()">Calculate TDEE</button>
""",


"body-fat": """
<label>Sex</label>
<select id="gender">
<option value="male">Male</option>
<option value="female">Female</option>
</select>

<label>Age</label>
<input id="age" type="number" min="1">

<label>BMI</label>
<input id="bmi" type="number" step="0.1" min="1" placeholder="Example: 23.5">

<button onclick="calculate()">Estimate Body Fat</button>
""",


"pace": """
<label>Distance (km)</label>
<input id="distance" type="number" step="0.01" min="0.01" placeholder="Example: 5">

<label>Time - Minutes</label>
<input id="minutes" type="number" min="0" placeholder="Example: 30">

<label>Additional Seconds</label>
<input id="seconds" type="number" min="0" max="59" placeholder="Example: 30">

<button onclick="calculate()">Calculate Pace</button>
""",


"steps-calories": """
<label>Steps</label>
<input id="steps" type="number" min="1" placeholder="Example: 10000">

<label>Body Weight (kg)</label>
<input id="weight" type="number" min="1" placeholder="Example: 70">

<button onclick="calculate()">Calculate Calories</button>
""",


"heart-rate": """
<label>Age</label>
<input id="age" type="number" min="1" placeholder="Example: 40">

<button onclick="calculate()">Calculate Heart Rate</button>
"""

}


# =========================================================
# CREATE HTML
# =========================================================

def create_html(tool):

    slug = tool["slug"]

    url = (
        SITE_URL
        + "/tools/"
        + slug
        + "/"
    )

    return f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>{tool["title"]}</title>

<meta name="description"
content="{tool["description"]}">

<meta name="robots"
content="index,follow">

<link rel="canonical"
href="{url}">

{CSS}

<script type="application/ld+json">
{{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": {json.dumps(tool["name"])},
    "url": {json.dumps(url)},
    "applicationCategory": "HealthApplication",
    "operatingSystem": "Web",
    "description": {json.dumps(tool["description"])}
}}
</script>

</head>

<body>

<header>

<nav>

<a href="/">HealthMelo</a>

<a href="/pages/health/">Health</a>

<a href="/pages/nutrition/">Nutrition</a>

<a href="/pages/fitness/">Fitness</a>

<a href="/tools/">Health Tools</a>

</nav>

</header>


<main>

<div class="card">

<p>
<a href="/">Home</a> /
<a href="/tools/">Tools</a> /
{tool["name"]}
</p>

<h1>{tool["name"]}</h1>

<p>
{tool["intro"]}
</p>

</div>


<div class="card">

<h2>Calculator</h2>

{FORMS[slug]}

<div
id="result"
class="result">
Your result will appear here.
</div>

</div>


<div class="card">

<h2>About this calculator</h2>

<p>
{tool["formula"]}
</p>

<p>
Results from this calculator are estimates for educational purposes.
Individual needs can vary based on health, medications, fitness level,
body composition and other factors.
</p>

</div>


<div class="card">

<h2>More HealthMelo Tools</h2>

<p>

<a href="/tools/bmi/">BMI Calculator</a> |
<a href="/tools/calorie/">Calorie Calculator</a> |
<a href="/tools/bmr/">BMR Calculator</a> |
<a href="/tools/water/">Water Intake Calculator</a> |
<a href="/tools/ideal-weight/">Ideal Weight Calculator</a>

</p>

</div>


<div class="note">

<strong>Health information notice:</strong>

HealthMelo calculators provide general educational estimates.
They are not a diagnosis or a substitute for individualized medical
advice. Consult a qualified healthcare professional for personal
health concerns.

</div>

</main>


<footer>

<p>
HealthMelo — Health Made Simple.
</p>

<p>

<a href="/pages/about/">About</a> |
<a href="/pages/contact/">Contact</a> |
<a href="/pages/privacy/">Privacy</a> |
<a href="/pages/disclaimer/">Disclaimer</a>

</p>

</footer>


<script>

{JS[slug]}

</script>

</body>

</html>
"""


# =========================================================
# BACKUP
# =========================================================

def backup_existing(path):

    if not path.exists():
        return

    relative = path.relative_to(ROOT)

    target = (
        BACKUP_DIR
        / relative
    )

    target.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    shutil.copy2(
        path,
        target
    )


# =========================================================
# MAIN
# =========================================================

def main():

    print()

    print("=" * 65)
    print("          HEALTHMELO TOOLS EXPANSION V10")
    print("=" * 65)

    print()

    print("[1/4] Preparing calculator expansion...")

    print(
        f"      Tools planned: {len(TOOLS)}"
    )

    print()

    print("[2/4] Creating calculators...")

    created = []
    skipped = []

    for tool in TOOLS:

        folder = (
            TOOLS_DIR
            / tool["slug"]
        )

        file = folder / "index.html"

        if file.exists():

            skipped.append(
                tool["slug"]
            )

            print(
                f"      SKIPPED: {tool['name']}"
            )

            continue

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        backup_existing(file)

        file.write_text(
            create_html(tool),
            encoding="utf-8"
        )

        created.append(
            tool["slug"]
        )

        print(
            f"      CREATED: {tool['name']}"
        )

    print()

    print("[3/4] Creating tool inventory...")

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    inventory = []

    for tool in TOOLS:

        inventory.append({

            "name": tool["name"],

            "slug": tool["slug"],

            "url":
                SITE_URL
                + "/tools/"
                + tool["slug"]
                + "/"

        })

    (
        REPORT_DIR
        / "V10-TOOLS-INVENTORY.json"
    ).write_text(
        json.dumps(
            inventory,
            indent=2
        ),
        encoding="utf-8"
    )

    print()

    print("[4/4] Writing report...")

    report = f"""# HealthMelo V10 Tool Expansion

Generated: {datetime.now()}

## Tools Planned

{chr(10).join("- " + x["name"] for x in TOOLS)}

## Summary

- Tools planned: {len(TOOLS)}
- New tools created: {len(created)}
- Existing tools skipped: {len(skipped)}

## New Tools

{chr(10).join("- /tools/" + x + "/" for x in created)}

## Safety

- Existing calculators were not overwritten.
- Existing HTML content was not deleted.
- Existing sitemap.xml was not modified.
- Existing robots.txt was not modified.
- Google verification file was not modified.
- New calculators contain educational-use disclaimers.
"""

    (
        REPORT_DIR
        / "V10-TOOLS-EXPANSION.md"
    ).write_text(
        report,
        encoding="utf-8"
    )

    print()

    print("=" * 65)
    print("                 V10 COMPLETE")
    print("=" * 65)

    print()

    print(
        f"Tools created: {len(created)}"
    )

    print(
        f"Tools skipped: {len(skipped)}"
    )

    print()

    print(
        "Existing tools: PROTECTED"
    )

    print(
        "Existing sitemap.xml: UNCHANGED"
    )

    print(
        "Existing robots.txt: UNCHANGED"
    )

    print()

    print(
        "Reports:"
    )

    print(
        "seo_reports/V10-TOOLS-EXPANSION.md"
    )

    print(
        "seo_reports/V10-TOOLS-INVENTORY.json"
    )

    print()

    print("=" * 65)


if __name__ == "__main__":
    main()