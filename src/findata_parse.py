# import requests
import json

class FinData: 
    def __init__(self, findata): 
        self.findata = findata

def main(): 
    fin = open("data/aapl.json", "r")
    data = json.load(fin)
    
    # print(data['facts']['dei'].keys())
    gaap = data['facts']['us-gaap']

    for key in gaap.keys():
        if (gaap[key]['label'] == None) or (gaap[key]['label'].find("Deprecated") == -1):
           print(key)

if __name__ == "__main__": 
    main()

"""
def main(): 
    url = "http://data.sec.gov/api/xbrl/companyfacts/CIK" + "0000320193" + ".json"
    headers = { "User-Agent": "DBL dbl27@proton.me" }
    res = requests.get(url, headers=headers, verify=False)

    out = json.dumps(res.json())
    with open("data/aapl.json", "w") as fout: 
        fout.write(out)
        fout.close()

if __name__ == "__main__": 
    main()
"""