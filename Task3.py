import json
import sys


def parseTests(t):
    for j in t:
        if "value" in j:
            j["value"] = changeValue(j["id"])
        if "values" in j:
            parseTests(j.get("values"))


def changeValue(ids):
    for q in val["values"]:
        if ids == q["id"]:
            return q["value"]


if __name__ == "__main__":
    f1, f2 = sys.argv[1], sys.argv[2]
    with open(f1, "r") as t1, open(f2, "r") as v1, \
         open("report.json", "w") as r1:
        test = json.load(t1)
        val = json.load(v1)
        for i in test["tests"]:
            if "value" in i:
                i["value"] = changeValue(i["id"])
            if "values" in i:
                parseTests(i.get("values"))
        json.dump(test, r1, indent=2)
