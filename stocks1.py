"""Displays stock symbol, current price, change, day high, day low, volume, previous close, and trading date for a stock."""

import requests
from tabulate import tabulate

api_url_1 = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
response1 = requests.get(api_url_1)
data1 = response1.json()

filtered_data = [{
    "symbol": data1["Global Quote"]["01. symbol"],
    "current price": "$" + data1["Global Quote"]["05. price"],
    "change from yesterday": data1["Global Quote"]["10. change percent"],
    "day high": data1["Global Quote"]["03. high"],
    "day low": data1["Global Quote"]["04. low"],
    "volume": data1["Global Quote"]["06. volume"],
    "previous close": data1["Global Quote"]["08. previous close"],
    "Trading Date": data1["Global Quote"]["07. latest trading day"]
}]

table = tabulate(filtered_data, headers = "keys")

print(table)
