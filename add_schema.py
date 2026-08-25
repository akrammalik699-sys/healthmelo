import os
import json

# Schema Markup Data (JSON-LD)
schema_data = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "WebSite",
            "@id": "https://healthmelo.com/#website",
            "url": "https://healthmelo.com/",
            "name": "Healthmelo",
            "description": "स्वास्थ्य और फ़िटनेस से जुड़ी जानकारी"
        },
        {
            "@type": "Organization",
            "@id": "https://healthmelo.com/#organization",
            "name": "Healthmelo",
            "url": "https://healthmelo.com/"
        }
    ]
}

schema_script = f'\n<script type="application/ld+json">\n{json.dumps(schema_data, indent=2)}\n</script>\n'

# सभी HTML फ़ाइलों में कोड जोड़ने की प्रक्रिया
for file_name in os.listdir("."):
    if file_name.endswith(".html"):
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()

        if "application/ld+json" not in content:
            if "</head>" in content:
                new_content = content.replace("</head>", f"{schema_script}</head>")
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"स्कीमा जुड़ गया: {file_name}")
            else:
                print(f"छोड़ दिया (Head टैग नहीं मिला): {file_name}")
        else:
            print(f"स्कीमा पहले से मौजूद है: {file_name}")
