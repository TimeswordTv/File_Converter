import sys
import csv
import json
import os

def convert_value(value):
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value

if len(sys.argv) != 3:
    print('\nUser Error:\n-- Usage: python convert.py input.csv output.json\nor\n-- Usage: python convert.py input.json output.csv\n')
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Get file extension
ext = os.path.splitext(input_file)[1].lower() # .csv or .json

if ext == '.csv':
    # Read CSV
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            convert_row = {k: convert_value(v) for k, v in row.items()}
            data.append(convert_row)
    # Write JSON
    with open(output_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)
    print(f"Converted CSV -> JSON: {output_file}")

elif ext == '.json':
    with open(input_file, 'r') as jsonfile:
        data = json.load(jsonfile)

    fieldnames = data[0].keys() if data else []

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Converted JSON -> CSV: {output_file}")

else:
    print('Unsuported file type! Use a .csv or .json file.')
