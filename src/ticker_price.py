from yfinance import Ticker
import json

with open("data/cik-ticker-mapping.json", "r") as fin: 
      data = json.load(fin)

for eq in data['data']: 
    if eq[3] == "Nasdaq" or eq[3] == 'NYSE': 
        tkr = Ticker(eq[2])
        tkr = tkr.info  

        price = round((tkr['bid'] + tkr['ask']) / 2, 2)

        print(eq[2] + "  ---  " + str(price))