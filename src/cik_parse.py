import json

with open("data/cik-ticker-mapping.json", "r") as cik_data:
    data = json.load(cik_data)

for entry in data['data']: 
    if entry[3] == "Nasdaq" or entry[3] == "NYSE": 
        print(entry[2])