from pathlib import Path
import collections

files = []

for p in Path(".").rglob("*.html"):
    s = str(p).replace("\\", "/")

    if "_backup" in s:
        continue

    if p.name.endswith((".backup", ".bad", ".encoding-backup")):
        continue

    if p.name == "google6dac5feead5d9a65.html":
        continue

    files.append(p)

groups = collections.Counter()

for p in files:
    s = str(p).replace("\\", "/")

    if "/tools/" in s:
        groups["tools"] += 1
    elif "/pages/hi/" in s:
        groups["hindi"] += 1
    elif "/pages/health/" in s:
        groups["english-health"] += 1
    else:
        groups["other"] += 1

print("==========================================")
print("       HEALTHMELO TOPIC MAP")
print("==========================================")
print("Actual pages:", len(files))
print()

for k, v in groups.items():
    print(f"{k}: {v}")

print()
print("URLS")
print("------------------------------------------")

for p in sorted(files):
    print(str(p).replace("\\", "/"))
