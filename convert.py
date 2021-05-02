import csv
import glob
import json

files = glob.glob("*.json")

data = []

for filename in files:
    timestamp = filename.rstrip(".json")
    with open(filename) as f:
        entry = json.load(f)
    
    data.append((timestamp, entry))

data = sorted(data, key=lambda x: x[0])

rows = []
for timestamp, log in data:
    log = log['data']
    row = {}
    row['timestamp'] = timestamp
    for slot in log:
        column = f"{slot['location']},{slot['date']}"
        row[column] = slot['balance']
    rows.append(row)

columns = list(rows[0].keys())
columns.remove('timestamp')
columns = sorted(columns)
columns.insert(0, 'timestamp')

with open("data.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, columns)
    writer.writeheader()
    writer.writerows(rows)
