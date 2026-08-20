import os
import csv
import json

CSV_DIR = "generated_level_question_csvs"
os.makedirs(CSV_DIR, exist_ok=True)

for filename in os.listdir(CSV_DIR):
    if filename.endswith(".csv"):
        filepath = os.path.join(CSV_DIR, filename)
        json_filename = filename.replace(".csv", ".json")
        json_filepath = os.path.join(CSV_DIR, json_filename)
        
        with open(filepath, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
        with open(json_filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            
        print(f"Converted {filename} to {json_filename}")
        os.remove(filepath)
        print(f"Deleted {filename}")

print("All CSV files converted to JSON.")
