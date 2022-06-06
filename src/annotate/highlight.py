from difflib import unified_diff
import json
import re

with open("data/training_data_gender.json", "r") as f:
    data = json.load(f)


def added_words(diff):
    words = []
    current = ""
    for c in diff:
        if c[0] in ["+"]:
            current += c[1]
        else:
            if len(current) > 3:
                words.append(current)
            current = ""
    return words


for item in data[:5]:
    y_ = item["y"]
    for w in added_words(unified_diff(item["x"], item["y"])):
        y_ = re.sub(w, f"<b>{w}</b>", item["y"])
    item["y_highlighted"] = y_

with open("data/training_data_gender_highlighted.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
