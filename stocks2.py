"""Displays symbol, name, price, analyst target price, volume, market capital, 52 week low/hihg, and whether to buy or sell a stock."""

import requests
from tabulate import tabulate

api_url_1 = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
api_url_2 = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
response1 = requests.get(api_url_1)
response2 = requests.get(api_url_2)
data1 = response1.json()
data2 = response2.json()

buy = ""

if float(data2["AnalystTargetPrice"]) * 0.95 > float(data1["Global Quote"]["05. price"]):
    buy = "Buy"
else:
    buy = "Sell"

filtered_data = [{
    "Stock Symbol": data2["Symbol"],
    "Company Name": data2["Name"],
    "Current Price": "$" + data1["Global Quote"]["05. price"],
    "Analyst Target Price": data2["AnalystTargetPrice"],
    "Volume": data1["Global Quote"]["06. volume"],
    "Market Capital": data2["MarketCapitalization"],
    "52 Week Low": data2["52WeekLow"],
    "52 Week High": data2["52WeekHigh"],
    "Buy/Sell": buy
    }]

table = tabulate(filtered_data, headers = "keys")

print(table)