from pathlib import Path
import re, shutil, datetime, json

ROOT = Path(".")
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup = ROOT / f"_backup_faq_{stamp}"
backup.mkdir(exist_ok=True)

FAQS = {
"fever": [
("What should I do for a fever at home?", "Rest, drink enough fluids, monitor your symptoms and follow appropriate medicine directions when needed. Seek medical advice if the fever is severe, persistent or accompanied by warning signs."),
("When should I worry about a fever?", "Seek medical care when fever is severe or persistent, or when it occurs with trouble breathing, confusion, severe dehydration, seizures, a stiff neck or other serious symptoms."),
("How long does a fever usually last?", "The duration depends on the underlying cause. Many short-term infections improve within several days, but persistent or worsening fever should be evaluated by a healthcare professional.")
],
"headache": [
("What are common causes of headache?", "Common causes include stress, lack of sleep, dehydration, skipped meals, eye strain and infections. Frequent or severe headaches may have other causes and should be evaluated."),
("How can I get headache relief at home?", "Rest, hydration, regular meals, sleep and reducing common triggers may help some everyday headaches."),
("When should a headache be checked urgently?", "A sudden extremely severe headache, headache after serious injury, or headache with weakness, confusion, fainting, seizures or other neurological symptoms needs urgent medical evaluation.")
],
"cough": [
("What can help a cough at home?", "Rest, adequate fluids and avoiding smoke or other irritants may help. The right treatment depends on the cause of the cough."),
("How long can a cough last?", "A cough can last from several days to weeks depending on its cause. A persistent, worsening or unexplained cough should be evaluated."),
("When should I see a doctor for a cough?", "Seek medical advice for breathing difficulty, chest pain, coughing blood, high or persistent fever, or a cough that is persistent or getting worse.")
],
"constipation": [
("What helps constipation naturally?", "Adequate fluids, gradually increasing dietary fiber and regular physical activity can help many people maintain regular bowel movements."),
("How much fiber should I get?", "Fiber needs vary by age and individual factors. Increase fiber gradually and drink enough fluids to reduce the chance of discomfort."),
("When is constipation serious?", "Seek medical advice for severe abdominal pain, vomiting, blood in stool, unexplained weight loss or persistent constipation.")
],
"dehydration": [
("What are common signs of dehydration?", "Thirst, dry mouth, dark urine, tiredness, dizziness and reduced urination can occur with dehydration."),
("How can I prevent dehydration?", "Drink fluids regularly and increase fluid intake when appropriate during heat, exercise, fever, vomiting or diarrhea."),
("When is dehydration an emergency?", "Severe weakness, confusion, fainting, very little urination or inability to keep fluids down can require urgent medical attention.")
],
"diarrhea": [
("What should I eat during diarrhea?", "Choose foods and fluids that are easy to tolerate and focus on replacing lost fluids and electrolytes."),
("How can I prevent dehydration from diarrhea?", "Drink fluids regularly and consider oral rehydration solutions when appropriate, especially when fluid losses are significant."),
("When should diarrhea be checked by a doctor?", "Seek medical advice for blood in stool, severe dehydration, severe abdominal pain, persistent symptoms or high fever.")
],
"bloating": [
("What commonly causes bloating?", "Gas, eating quickly, certain foods, constipation and changes in digestion can contribute to bloating."),
("How can I reduce bloating?", "Eating slowly, staying active, identifying personal food triggers and addressing constipation may help."),
("When should bloating be checked?", "Persistent or severe bloating, especially with significant pain, vomiting, blood in stool or unexplained weight loss, should be evaluated.")
],
"dizziness": [
("What can cause dizziness?", "Dehydration, low blood pressure, illness, medication effects and inner-ear problems are among possible causes."),
("What should I do when I feel dizzy?", "Sit or lie down safely, avoid driving and consider whether dehydration or another obvious trigger may be involved."),
("When is dizziness an emergency?", "Dizziness with fainting, chest pain, severe headache, weakness, difficulty speaking or other serious symptoms needs urgent medical evaluation.")
],
"fatigue": [
("What are common causes of fatigue?", "Poor sleep, stress, inadequate nutrition, infections and many other conditions can cause fatigue."),
("How can I improve everyday fatigue?", "Regular sleep, balanced meals, hydration, physical activity and managing stress may help when lifestyle factors contribute."),
("When should fatigue be evaluated?", "Persistent, severe or unexplained fatigue, especially with other concerning symptoms, should be discussed with a healthcare professional.")
],
"sore-throat": [
("What helps a sore throat at home?", "Fluids, rest and soothing measures such as warm drinks may provide relief for some people."),
("How long does a sore throat last?", "Many short-term sore throats improve within several days, depending on the cause."),
("When should a sore throat be checked?", "Difficulty breathing or swallowing, severe symptoms, dehydration or persistent/worsening symptoms require medical assessment.")
],
"stomach-pain": [
("What can cause stomach pain?", "Indigestion, gas, constipation, infections and many other conditions can cause abdominal discomfort."),
("What can I do for mild stomach pain?", "Rest, hydration and avoiding foods that clearly worsen symptoms may help mild discomfort."),
("When is stomach pain urgent?", "Severe or sudden pain, persistent vomiting, blood in vomit or stool, fainting or other serious symptoms require urgent medical evaluation.")
],
"joint-pain": [
("What commonly causes joint pain?", "Overuse, injuries, inflammation and several medical conditions can cause joint pain."),
("What can help mild joint pain?", "Rest from aggravating activity, appropriate movement and other supportive measures may help depending on the cause."),
("When should joint pain be evaluated?", "Persistent, severe or worsening pain, major swelling, redness, fever or inability to use the joint should be medically evaluated.")
],
"sleep": [
("How many hours of sleep do adults need?", "Most adults generally need around 7 to 9 hours of sleep each night, although individual needs vary."),
("How can I improve sleep naturally?", "A consistent sleep schedule, a comfortable sleep environment, limiting late caffeine and reducing stimulating activities before bed can help."),
("When should sleep problems be checked?", "Persistent insomnia, loud snoring with breathing pauses, excessive daytime sleepiness or other ongoing sleep problems should be evaluated.")
],
"stress": [
("What are simple ways to manage stress?", "Regular movement, adequate sleep, relaxation techniques, social support and healthy routines can help manage everyday stress."),
("Can stress affect sleep?", "Yes. Stress can make it harder to fall asleep, stay asleep or feel rested."),
("When should I seek help for stress?", "If stress is persistent, overwhelming or significantly affecting daily life, professional support can be helpful.")
]
}

files = [
    p for p in ROOT.rglob("*.html")
    if "_backup" not in str(p)
    and not p.name.endswith((".backup",".bad",".encoding-backup"))
    and p.name != "google6dac5feead5d9a65.html"
]

changed = 0

for p in files:
    path = str(p).replace("\\","/")

    if "/pages/health/guides/" not in path:
        continue

    slug = p.parent.name.lower()

    if slug not in FAQS:
        continue

    s = p.read_text(encoding="utf-8", errors="ignore")

    if "HealthMelo Long-Tail FAQ" in s:
        continue

    hindi = "/pages/hi/" in path

    if hindi:
        title = "अक्सर पूछे जाने वाले सवाल"
        intro = "इन सामान्य सवालों के जवाब आपको इस विषय को बेहतर समझने में मदद कर सकते हैं।"
        faq_items = [
            ("इस विषय के सामान्य सवाल क्या हैं?", "लक्षण, कारण और देखभाल व्यक्ति और स्थिति के अनुसार अलग हो सकते हैं। लगातार या गंभीर समस्या में स्वास्थ्य विशेषज्ञ से सलाह लें।"),
            ("घर पर क्या ध्यान रखना चाहिए?", "आराम, पर्याप्त पानी और स्वस्थ दिनचर्या मदद कर सकती है। गंभीर या बिगड़ते लक्षणों में चिकित्सकीय सलाह लें।"),
            ("डॉक्टर से कब संपर्क करना चाहिए?", "गंभीर, लगातार या तेजी से बिगड़ते लक्षणों में स्वास्थ्य विशेषज्ञ से संपर्क करना चाहिए।")
        ]
    else:
        title = "Frequently Asked Questions"
        intro = "These common questions provide practical context and help you understand this health topic."
        faq_items = FAQS[slug]

    html = [
        '<section class="healthmelo-faq">',
        f"<h2>{title}</h2>",
        f"<p>{intro}</p>"
    ]

    schema_items = []

    for q, a in faq_items:
        html.append(f"<h3>{q}</h3>")
        html.append(f"<p>{a}</p>")
        schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    html.append("</section>")
    html.append("<!-- HealthMelo Long-Tail FAQ -->")

    block = "\n".join(html)

    if "</main>" in s:
        s = s.replace("</main>", block + "\n</main>", 1)
    else:
        s = s.replace("</body>", block + "\n</body>", 1)

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": schema_items
    }

    s = s.replace(
        "</head>",
        '<script type="application/ld+json">' +
        json.dumps(schema, ensure_ascii=False) +
        "</script>\n</head>",
        1
    )

    dest = backup / p.relative_to(ROOT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)

    p.write_text(s, encoding="utf-8")
    changed += 1

print("="*60)
print("HEALTHMELO LONG-TAIL FAQ SEO UPGRADE")
print("="*60)
print("FAQ pages upgraded:", changed)
print("Backup:", backup)
print("Added: search-intent FAQs + FAQ structured data")
print("No existing pages deleted.")
print()
print("NEXT:")
print("python healthmelo_final_audit.py")
