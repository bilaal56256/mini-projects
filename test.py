import os
import json
import datetime
filepath = "s.json"
if os.path.exists(filepath):
    with open(filepath, "r") as file:
        content = json.load(file)
for index, i in enumerate(content, start=1):
    if i["a"] == 1:
        print(f"{index}.")
        for key, value in i.items():
            print(f"{key}: {value}")
        print()