import csv
import json

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

with open("students.json", "w") as file:
        json.dump(data, file, indent=4)
        