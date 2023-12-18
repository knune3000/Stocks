"""Displays symbol, name, 52 week low/high, and analyst target price of a stock."""

import requests
from tabulate import tabulate

api_url_1 = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
api_url_2 = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
response1 = requests.get(api_url_1)
response2 = requests.get(api_url_2)
data1 = response1.json()
data2 = response2.json()

filtered_data = [{
    "Stock Symbol": data2["Symbol"],
    "Company Name": data2["Name"],
    "Market Capital": data2["MarketCapitalization"],
    "52 Week Low": data2["52WeekLow"],
    "52 Week High": data2["52WeekHigh"],
    "Analyst Target Price": data2["AnalystTargetPrice"]
}]

table = tabulate(filtered_data, headers = "keys")

print(table)