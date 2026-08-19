from pathlib import Path
from datetime import datetime
import json


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://legendary-llama-0aca4c.netlify.app"

REPORT_DIR = ROOT / "seo_reports"

TARGET = ROOT / "pages" / "hi" / "guides"


ARTICLES = [
    {
        "slug": "healthy-eating",
        "title": "स्वस्थ भोजन क्या है? संतुलित आहार की आसान जानकारी",
        "description": "स्वस्थ भोजन, संतुलित आहार, पोषक खाद्य पदार्थ और रोज़ाना खाने की आसान आदतों के बारे में सरल जानकारी।",
        "intro": "स्वस्थ भोजन का मतलब केवल कम खाना या किसी एक खाद्य पदार्थ को छोड़ना नहीं है। संतुलित आहार में अलग-अलग प्रकार के पौष्टिक खाद्य पदार्थ शामिल करना महत्वपूर्ण है।",
        "sections": [
            ("संतुलित आहार क्या है?", "संतुलित आहार में सब्जियां, फल, साबुत अनाज, प्रोटीन वाले खाद्य पदार्थ और उचित मात्रा में स्वस्थ वसा जैसे अलग-अलग खाद्य समूह शामिल हो सकते हैं।"),
            ("प्लेट को संतुलित कैसे रखें?", "भोजन में सब्जियों या फलों के साथ प्रोटीन और अनाज या अन्य कार्बोहाइड्रेट स्रोत शामिल करना एक व्यावहारिक तरीका हो सकता है।"),
            ("पौष्टिक भोजन चुनें", "दालें, फलियां, सब्जियां, फल, साबुत अनाज, अंडे, दूध या अन्य प्रोटीन स्रोत शरीर को कई जरूरी पोषक तत्व दे सकते हैं।"),
            ("रोज़ की अच्छी आदतें", "नियमित भोजन, पर्याप्त पानी, विविध खाद्य पदार्थ और बहुत अधिक मीठे या अत्यधिक प्रोसेस्ड खाद्य पदार्थों को सीमित करना उपयोगी आदतें हो सकती हैं।"),
            ("व्यक्तिगत सलाह कब जरूरी है?", "यदि किसी व्यक्ति को कोई बीमारी, खाद्य एलर्जी या विशेष पोषण संबंधी आवश्यकता है, तो योग्य स्वास्थ्य विशेषज्ञ या डाइटिशियन से व्यक्तिगत सलाह लेना बेहतर है।")
        ]
    },
    {
        "slug": "hydration-guide",
        "title": "पानी और हाइड्रेशन: शरीर को पर्याप्त पानी कैसे दें",
        "description": "पानी पीने, हाइड्रेशन, डिहाइड्रेशन के संकेत और रोज़ाना पर्याप्त तरल लेने की आसान जानकारी।",
        "intro": "पानी शरीर के कई सामान्य कार्यों के लिए जरूरी है। हर व्यक्ति की पानी की जरूरत उम्र, गतिविधि, मौसम और स्वास्थ्य स्थिति के अनुसार अलग हो सकती है।",
        "sections": [
            ("पानी क्यों जरूरी है?", "पानी शरीर के तापमान को नियंत्रित करने, सामान्य रक्त संचार और अन्य शारीरिक प्रक्रियाओं में महत्वपूर्ण भूमिका निभाता है।"),
            ("डिहाइड्रेशन के संकेत", "प्यास, मुंह का सूखना, पेशाब का रंग गहरा होना या पेशाब कम आना शरीर में पर्याप्त तरल न होने के संकेत हो सकते हैं।"),
            ("पानी पीने की आसान आदतें", "दिनभर पानी पास रखें, भोजन के साथ पानी लें और गर्म मौसम या शारीरिक गतिविधि के दौरान तरल पदार्थों पर अधिक ध्यान दें।"),
            ("व्यायाम और पानी", "लंबे या अधिक मेहनत वाले व्यायाम तथा गर्म वातावरण में शरीर से अधिक तरल निकल सकता है। जरूरत व्यक्ति और परिस्थिति के अनुसार बदलती है।"),
            ("कब डॉक्टर से संपर्क करें?", "बहुत ज्यादा कमजोरी, भ्रम, बेहोशी या गंभीर डिहाइड्रेशन जैसे लक्षण होने पर तुरंत चिकित्सा सहायता लेना जरूरी हो सकता है।")
        ]
    },
    {
        "slug": "sleep-hygiene",
        "title": "अच्छी नींद के लिए Sleep Hygiene की आसान जानकारी",
        "description": "बेहतर नींद के लिए नियमित समय, शांत वातावरण और स्वस्थ sleep habits के बारे में आसान जानकारी।",
        "intro": "अच्छी नींद शरीर, मूड, ध्यान और रोज़मर्रा की कार्यक्षमता के लिए महत्वपूर्ण है। कुछ सरल आदतें नियमित और आरामदायक नींद में मदद कर सकती हैं।",
        "sections": [
            ("सोने और उठने का समय तय रखें", "हर दिन लगभग एक ही समय पर सोने और उठने की आदत शरीर की नियमित नींद की दिनचर्या बनाने में मदद कर सकती है।"),
            ("सोने से पहले शांत रहें", "सोने से पहले शांत गतिविधियां जैसे पढ़ना या आराम करना शरीर और दिमाग को नींद के लिए तैयार कर सकता है।"),
            ("बेडरूम का वातावरण", "शांत, आरामदायक और जरूरत के अनुसार अंधेरा वातावरण नींद के लिए मददगार हो सकता है।"),
            ("कैफीन पर ध्यान दें", "कुछ लोगों में देर से लिया गया कैफीन नींद को प्रभावित कर सकता है। इसलिए अपनी व्यक्तिगत प्रतिक्रिया को ध्यान में रखना उपयोगी है।"),
            ("लगातार नींद की समस्या", "यदि नींद की समस्या बार-बार होती है या दिनभर की गतिविधियों को प्रभावित करती है, तो स्वास्थ्य विशेषज्ञ से बात करें।")
        ]
    },
    {
        "slug": "stress-management",
        "title": "तनाव कम करने के आसान तरीके और स्वस्थ आदतें",
        "description": "रोज़मर्रा के तनाव को संभालने, आराम करने और मानसिक स्वास्थ्य को बेहतर तरीके से सपोर्ट करने की आसान जानकारी।",
        "intro": "तनाव चुनौतीपूर्ण परिस्थितियों के प्रति शरीर और मन की सामान्य प्रतिक्रिया हो सकता है। स्वस्थ coping habits रोज़मर्रा के तनाव को संभालने में मदद कर सकती हैं।",
        "sections": [
            ("तनाव के कारण पहचानें", "कौन-सी परिस्थितियां बार-बार तनाव बढ़ाती हैं, यह पहचानना समस्या को समझने और व्यावहारिक बदलाव करने में मदद कर सकता है।"),
            ("आराम की तकनीकें", "धीमी सांस लेना, हल्की वॉक, स्ट्रेचिंग और कुछ समय शांत रहना तत्काल तनाव कम करने में मदद कर सकता है।"),
            ("अपनों से बात करें", "विश्वसनीय परिवार, दोस्तों या अन्य सहायक लोगों से बात करना कठिन समय में भावनात्मक सहयोग दे सकता है।"),
            ("स्वस्थ दिनचर्या रखें", "अच्छी नींद, पौष्टिक भोजन, नियमित गतिविधि और व्यवस्थित दिनचर्या शरीर और मन को सपोर्ट कर सकती है।"),
            ("कब मदद लें?", "यदि तनाव बहुत अधिक हो, लंबे समय तक बना रहे या रोज़मर्रा की जिंदगी को गंभीर रूप से प्रभावित करे, तो योग्य मानसिक स्वास्थ्य विशेषज्ञ से सहायता लेना उचित है।")
        ]
    },
    {
        "slug": "constipation-prevention",
        "title": "कब्ज से बचाव: फाइबर, पानी और रोज़ की आदतें",
        "description": "कब्ज से बचने के लिए फाइबर, पानी, शारीरिक गतिविधि और स्वस्थ bowel habits के बारे में जानकारी।",
        "intro": "कब्ज में मल कठोर होना, मल त्याग में कठिनाई या सामान्य से कम बार मल त्याग होना शामिल हो सकता है। कुछ रोज़मर्रा की आदतें नियमित bowel movement को सपोर्ट कर सकती हैं।",
        "sections": [
            ("फाइबर वाला भोजन", "सब्जियां, फल, दालें, फलियां और साबुत अनाज फाइबर के अच्छे स्रोत हो सकते हैं। फाइबर धीरे-धीरे बढ़ाना उपयोगी होता है।"),
            ("पर्याप्त पानी लें", "फाइबर बढ़ाने के साथ पर्याप्त तरल लेना भी जरूरी हो सकता है। पानी की जरूरत व्यक्ति और परिस्थिति के अनुसार अलग होती है।"),
            ("शारीरिक गतिविधि", "नियमित चलना और अन्य शारीरिक गतिविधियां सामान्य bowel function को सपोर्ट कर सकती हैं।"),
            ("मल त्याग की इच्छा न रोकें", "बार-बार मल त्याग की इच्छा को रोकना कुछ लोगों में bowel habits को प्रभावित कर सकता है।"),
            ("कब डॉक्टर से मिलें?", "तेज पेट दर्द, उल्टी, मल में खून, बिना कारण वजन कम होना या लंबे समय तक कब्ज रहने पर स्वास्थ्य विशेषज्ञ से सलाह लें।")
        ]
    },
    {
        "slug": "common-cold-care",
        "title": "सर्दी-जुकाम में घर पर देखभाल: क्या मदद कर सकता है?",
        "description": "सर्दी-जुकाम के लक्षणों में आराम, पानी और सामान्य self-care के बारे में आसान स्वास्थ्य जानकारी।",
        "intro": "सर्दी-जुकाम आमतौर पर वायरल संक्रमण से जुड़ा होता है। ज्यादातर मामलों में समय और supportive care से सुधार हो सकता है।",
        "sections": [
            ("आराम और पानी", "पर्याप्त आराम और तरल पदार्थ लेना शरीर को recovery के दौरान सपोर्ट कर सकता है।"),
            ("नाक बंद और गले की परेशानी", "गुनगुने तरल और उपयुक्त saline nasal उपाय कुछ लोगों को लक्षणों में आराम दे सकते हैं।"),
            ("खांसी", "जुकाम के दौरान खांसी हो सकती है और इसे ठीक होने में समय लग सकता है। धुएं और अन्य respiratory irritants से बचना उपयोगी हो सकता है।"),
            ("संक्रमण फैलने से बचें", "हाथ साफ रखना, खांसते या छींकते समय मुंह ढकना और बीमार होने पर दूसरों से दूरी रखना संक्रमण फैलने का जोखिम कम कर सकता है।"),
            ("कब चिकित्सा सहायता लें?", "सांस लेने में कठिनाई, गंभीर डिहाइड्रेशन या लक्षणों के लगातार बिगड़ने पर स्वास्थ्य विशेषज्ञ से संपर्क करें।")
        ]
    },
    {
        "slug": "fever-guide",
        "title": "बुखार: कारण, घर पर देखभाल और चेतावनी संकेत",
        "description": "बुखार क्या है, supportive care कैसे करें और किन लक्षणों में चिकित्सा सहायता जरूरी हो सकती है।",
        "intro": "बुखार शरीर के तापमान में सामान्य से वृद्धि है और यह कई संक्रमणों या अन्य स्थितियों के साथ हो सकता है। केवल तापमान ही नहीं, व्यक्ति की पूरी स्थिति देखना महत्वपूर्ण है।",
        "sections": [
            ("बुखार क्या है?", "बुखार शरीर के तापमान में वृद्धि है और यह अक्सर संक्रमण के प्रति शरीर की प्रतिक्रिया से जुड़ा होता है।"),
            ("घर पर देखभाल", "आराम, आरामदायक कपड़े और पर्याप्त तरल लेना supportive care का हिस्सा हो सकता है।"),
            ("पूरी स्थिति देखें", "तापमान के साथ सांस लेने, होश, कमजोरी, पानी की कमी और अन्य लक्षणों पर ध्यान देना जरूरी है।"),
            ("बच्चों और बुजुर्गों में ध्यान", "उम्र और पहले से मौजूद स्वास्थ्य स्थितियां बुखार के मूल्यांकन को प्रभावित कर सकती हैं।"),
            ("चेतावनी संकेत", "सांस लेने में परेशानी, भ्रम, बेहोशी, गंभीर कमजोरी, दौरे या गंभीर डिहाइड्रेशन जैसे लक्षणों में तुरंत चिकित्सा सहायता लें।")
        ]
    },
    {
        "slug": "headache-guide",
        "title": "सिरदर्द: सामान्य कारण और Self-Care Tips",
        "description": "सिरदर्द के सामान्य triggers, पानी, नींद और रोज़मर्रा की self-care आदतों की जानकारी।",
        "intro": "सिरदर्द आम समस्या है और इसके कई कारण हो सकते हैं। अपने triggers पहचानना और स्वस्थ दिनचर्या बनाए रखना कुछ लोगों के लिए उपयोगी हो सकता है।",
        "sections": [
            ("सामान्य triggers", "डिहाइड्रेशन, नींद की कमी, भोजन छोड़ना, तनाव और लंबे समय तक स्क्रीन देखना कुछ लोगों में सिरदर्द से जुड़े हो सकते हैं।"),
            ("रोज़मर्रा की आदतें", "नियमित भोजन, पर्याप्त पानी, अच्छी नींद और स्क्रीन से बीच-बीच में ब्रेक लेना मददगार हो सकता है।"),
            ("Headache diary रखें", "सिरदर्द कब हुआ, कितनी देर रहा और उससे पहले क्या हुआ था, यह लिखना patterns पहचानने में मदद कर सकता है।"),
            ("दवाओं का अधिक उपयोग न करें", "बार-बार कुछ pain medicines लेने से medication-overuse headache हो सकता है। दवा के निर्देशों का पालन करें।"),
            ("खतरे के संकेत", "अचानक बहुत तेज सिरदर्द, सिर पर गंभीर चोट के बाद सिरदर्द, बेहोशी, भ्रम या नए neurological symptoms होने पर तत्काल चिकित्सा सहायता लें।")
        ]
    },
    {
        "slug": "healthy-weight",
        "title": "स्वस्थ वजन: BMI, कैलोरी और रोज़ की आदतें",
        "description": "BMI, कैलोरी, शारीरिक गतिविधि और स्वस्थ वजन बनाए रखने की बुनियादी जानकारी।",
        "intro": "स्वस्थ वजन कई चीजों से प्रभावित होता है, जैसे भोजन, गतिविधि, नींद, आनुवंशिकी, दवाएं और स्वास्थ्य स्थितियां। कोई एक संख्या पूरी सेहत को परिभाषित नहीं करती।",
        "sections": [
            ("BMI क्या है?", "BMI लंबाई और वजन पर आधारित एक screening measure है। यह उपयोगी हो सकता है लेकिन अकेले शरीर की चर्बी या पूरी स्वास्थ्य स्थिति नहीं बताता।"),
            ("कैलोरी क्या होती है?", "शरीर अपनी सामान्य गतिविधियों और शारीरिक काम के लिए ऊर्जा इस्तेमाल करता है। भोजन ऊर्जा प्रदान करता है और हर व्यक्ति की जरूरत अलग हो सकती है।"),
            ("स्थायी आदतों पर ध्यान दें", "संतुलित भोजन, नियमित movement, अच्छी नींद और realistic routine लंबे समय के लिए अधिक उपयोगी हो सकते हैं।"),
            ("Health calculators का उपयोग", "कैलकुलेटर अनुमान और educational information दे सकते हैं। इन्हें diagnosis या व्यक्तिगत medical prescription नहीं मानना चाहिए।"),
            ("व्यक्तिगत सलाह", "यदि वजन तेजी से या बिना कारण बदल रहा है या कोई chronic condition है, तो स्वास्थ्य विशेषज्ञ से सलाह लेना बेहतर है।")
        ]
    },
    {
        "slug": "exercise-basics",
        "title": "व्यायाम की शुरुआत: Cardio, Strength और रोज़ की Activity",
        "description": "कार्डियो, strength training, flexibility और रोज़मर्रा की physical activity की आसान जानकारी।",
        "intro": "नियमित शारीरिक गतिविधि हृदय स्वास्थ्य, ताकत, mobility, mood और overall wellbeing को सपोर्ट कर सकती है।",
        "sections": [
            ("Cardio Exercise", "चलना, साइकिल चलाना, तैरना और ऐसी गतिविधियां जो heart rate बढ़ाती हैं cardiovascular fitness को सपोर्ट कर सकती हैं।"),
            ("Strength Training", "Resistance exercises मांसपेशियों की ताकत बनाए रखने या बढ़ाने में मदद कर सकते हैं। शुरुआत में हल्के resistance और सही technique पर ध्यान दें।"),
            ("Flexibility और Mobility", "हल्की stretching और mobility exercises comfortable movement बनाए रखने में मदद कर सकती हैं। दर्द होने पर range को force न करें।"),
            ("धीरे शुरुआत करें", "यदि आप लंबे समय से inactive हैं, तो activity को धीरे-धीरे बढ़ाना अचानक बहुत कठिन workout करने से बेहतर हो सकता है।"),
            ("सुरक्षा", "तेज दर्द, बेहोशी, गंभीर सांस की परेशानी या अन्य चिंताजनक लक्षण होने पर exercise रोकें और जरूरत पड़ने पर चिकित्सा सहायता लें।")
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


def make_html(article):

    sections = ""

    for heading, text in article["sections"]:
        sections += f"""
<section>
<h2>{esc(heading)}</h2>
<p>{esc(text)}</p>
</section>
"""

    return f"""<!DOCTYPE html>
<html lang="hi">
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
href="{SITE_URL}/pages/hi/guides/{article["slug"]}/">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {json.dumps(article["title"], ensure_ascii=False)},
  "description": {json.dumps(article["description"], ensure_ascii=False)},
  "inLanguage": "hi",
  "url": {json.dumps(SITE_URL + "/pages/hi/guides/" + article["slug"] + "/")},
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
<a href="/pages/hi/">HealthMelo हिंदी</a> |
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
<a href="/pages/hi/">हिंदी</a> /
<a href="/pages/hi/guides/">स्वास्थ्य गाइड</a>
</p>

<h1>{esc(article["title"])}</h1>

<p>{esc(article["intro"])}</p>

{sections}

<section>

<h2>HealthMelo के उपयोगी Tools</h2>

<p>
<a href="/tools/bmi/">BMI Calculator</a> |
<a href="/tools/calorie/">Calorie Calculator</a> |
<a href="/tools/water/">Water Intake Calculator</a>
</p>

</section>

<section>

<h2>महत्वपूर्ण स्वास्थ्य जानकारी</h2>

<p>
HealthMelo की जानकारी सामान्य शैक्षिक और informational purpose के लिए है।
यह diagnosis, treatment या व्यक्तिगत medical advice का विकल्प नहीं है।
व्यक्तिगत स्वास्थ्य समस्या के लिए qualified healthcare professional से सलाह लें।
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


def main():

    print()
    print("=" * 65)
    print("          HEALTHMELO HINDI EXPANSION V9")
    print("=" * 65)
    print()

    print("[1/4] Preparing Hindi content directory...")

    TARGET.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        f"      Hindi articles planned: {len(ARTICLES)}"
    )

    print("[2/4] Creating Hindi articles...")

    created = []

    for article in ARTICLES:

        folder = TARGET / article["slug"]
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
            make_html(article),
            encoding="utf-8"
        )

        created.append(
            article["slug"]
        )

    print(
        f"      Hindi articles created: {len(created)}"
    )

    print("[3/4] Creating Hindi inventory...")

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    inventory = []

    for article in ARTICLES:

        inventory.append({
            "slug": article["slug"],
            "title": article["title"],
            "language": "hi",
            "url": (
                SITE_URL
                + "/pages/hi/guides/"
                + article["slug"]
                + "/"
            )
        })

    (
        REPORT_DIR / "v9-hindi-inventory.json"
    ).write_text(
        json.dumps(
            inventory,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )

    print("[4/4] Writing report...")

    report = f"""# HealthMelo V9 Hindi Expansion

Generated: {datetime.now()}

## Summary

- Planned Hindi articles: {len(ARTICLES)}
- New Hindi articles created: {len(created)}

## Safety

- Existing pages were not overwritten.
- Existing English content was not deleted.
- Existing sitemap.xml was not modified.
- Existing robots.txt was not modified.
- Google verification file was not modified.
- New Hindi pages include canonical URLs.
- New Hindi pages include Article structured data.
- New Hindi pages include health disclaimer.
"""

    (
        REPORT_DIR / "V9-HINDI-EXPANSION.md"
    ).write_text(
        report,
        encoding="utf-8"
    )

    print()
    print("=" * 65)
    print("                 V9 COMPLETE")
    print("=" * 65)
    print()

    print(
        f"Hindi articles created: {len(created)}"
    )

    print(
        "Existing English content: PROTECTED"
    )

    print(
        "Existing sitemap.xml: UNCHANGED"
    )

    print(
        "Existing robots.txt: UNCHANGED"
    )

    print()

    print(
        "Report:"
    )

    print(
        "seo_reports/V9-HINDI-EXPANSION.md"
    )

    print()
    print("=" * 65)


if __name__ == "__main__":
    main()