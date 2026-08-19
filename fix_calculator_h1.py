from pathlib import Path
import re
import shutil

files = ["calorie", "bmr", "ideal-weight", "water"]
changed = []

for x in files:
    f = Path("tools") / x / "index.html"
    s = f.read_text(encoding="utf-8-sig")

    pattern = r"<h1[^>]*>\s*([^<]*?)\s+Calculator\s+Calculator\s*</h1>"

    if re.search(pattern, s, re.I):
        shutil.copy2(f, str(f) + ".backup_h1_20260813")

        s = re.sub(
            pattern,
            lambda m: "<h1>" + m.group(1).strip() + " Calculator</h1>",
            s,
            count=1,
            flags=re.I
        )

        f.write_text(s, encoding="utf-8")
        changed.append(x)

print("Fixed:", changed)