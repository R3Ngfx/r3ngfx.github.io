import os
import re

templates = []

for t in os.listdir("templates"):
    templates.append([t[0:-5], open(f"templates/{t}").read()[0:-1]])

for f in os.listdir("."):
    if not f.endswith(".html"):
        continue
    file = open(f, "r")
    contents = file.read()
    file.close()
    file = open(f, "w")
    for t in templates:
        toSub = f"<!-- {t[0]} start -->((.|\\n)*)<!-- {t[0]} end -->"
        contents = re.sub(toSub, t[1], contents)
        if re.compile(toSub).search(contents) != None:
            print(f"Added {t[0]} template to {f}")
    file.write(contents)
    file.close()

for f in os.listdir("blog"):
    if not f.endswith(".html"):
        continue
    f = "blog/"+f
    file = open(f, "r")
    contents = file.read()
    file.close()
    file = open(f, "w")
    for t in templates:
        toSub = f"<!-- {t[0]} start -->((.|\\n)*)<!-- {t[0]} end -->"
        contents = re.sub(toSub, t[1], contents)
        if re.compile(toSub).search(contents) != None:
            print(f"Added {t[0]} template to {f}")
    file.write(contents)
    file.close()
