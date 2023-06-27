import requests 
import json 

def main(): 
    cik_map_url = "https://www.sec.gov/files/company_tickers_exchange.json"
    cik_map_res = requests.get(cik_map_url, verify=False)

    with open("data/cik-ticker-mapping.json", "w") as fout: 
        out_data = json.dumps(cik_map_res.json())
        fout.write(out_data) 


    findata_url = "http://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json"
    findata_headers = { 'User-Agent': 'DBL dbl27@proton.me' }
    # findata_res = requests.get(findata_url, headers=findata_headers, verify=False)

if __name__ == "__main__":
    main()