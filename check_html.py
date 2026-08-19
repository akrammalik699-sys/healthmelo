from pathlib import Path
import re

f = Path("pages/hi/index.html")
s = f.read_text(encoding="utf-8", errors="replace")

print("BACKSLASH TAGS:", len(re.findall(r'\\(?:<!DOCTYPE|</?[A-Za-z]|<!--)', s)))
print("MARKDOWN URL:", "[https://" in s)
print("MOJIBAKE:", "à¤" in s)
