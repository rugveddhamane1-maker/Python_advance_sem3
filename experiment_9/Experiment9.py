import csv
import json

# Input and output file names
input_file = "student.csv"
output_file = "student.json"

# Read data from CSV file
with open(input_file, "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# Convert CSV data to JSON format
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")
print("JSON file created successfully:", output_file)