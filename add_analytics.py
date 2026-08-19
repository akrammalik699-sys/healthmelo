from pathlib import Path

TAG = """<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6LVMCEKWEN"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-6LVMCEKWEN');
</script>
<!-- End Google Analytics -->"""

count = 0

for p in Path(".").rglob("*.html"):

    text = p.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    if "<head" not in text.lower():
        continue

    if "G-6LVMCEKWEN" in text:
        continue

    pos = text.lower().find("<head>")

    if pos == -1:
        continue

    pos += len("<head>")

    new_text = (
        text[:pos]
        + "\n"
        + TAG
        + text[pos:]
    )

    p.write_text(
        new_text,
        encoding="utf-8"
    )

    count += 1

print()
print("Google Analytics added to:", count, "HTML files")
