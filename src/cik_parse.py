import json
import requests
import time 

class Equity: 
    def __init__(self, cik: str, ticker: str): 
        self.cik = cik
        self.ticker = ticker

with open("data/cik-ticker-mapping.json", "r") as cik_data:
    data = json.load(cik_data)

eq_list = []

for entry in data['data']: 
    if entry[3] == "Nasdaq" or entry[3] == "NYSE": 
        eq = Equity(entry[0], entry[2])
        eq_list.append(eq)

for eq in eq_list: 
    cik_str = str(eq.cik)

    findata_url = "http://data.sec.gov/api/xbrl/companyfacts/CIK" + ".json"
    findata_headers = { 'User-Agent': 'DBL dbl27@proton.me' }
    findata_res = requests.get(findata_url, headers=findata_headers)
