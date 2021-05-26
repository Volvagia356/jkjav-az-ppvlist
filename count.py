import glob
import json

files = glob.glob("2021-05-2*.json")

data = []

for filename in files:
    timestamp = filename.rstrip(".json")
    with open(filename) as f:
        try:
            entry = json.load(f)
        except:
            entry = {}
    
    data.append((timestamp, entry))

data = sorted(data, key=lambda x: x[0])

for timestamp, log in data:
    try:
        log = log['data']
    except KeyError:
        print(timestamp, "ERROR")
        continue
    count = 0
    for location in log:
        if location['available']:
            count += 1
    print(timestamp, count)
