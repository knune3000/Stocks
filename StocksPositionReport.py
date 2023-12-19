"""Displays stock position report based off of api url for that stock."""

import requests
from tabulate import tabulate
import random

api_url_1 = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
api_url_2 = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=AAPL&apikey=EMANGPF3LHEM5J6T"
response1 = requests.get(api_url_1)
response2 = requests.get(api_url_2)
data1 = response1.json()
data2 = response2.json()

profit = ""
change = float(data1["Global Quote"]["09. change"]) 
if change < 0:
    profit = "Loss"
elif change == 0:
    profit = "None"
else:
    profit = "Profit"

filtered_data = [{
    "Stock Symbol": data2["Symbol"],
    "Current Price": data1["Global Quote"]["05. price"],
    "52 Wk High": data2["52WeekHigh"],
    "Qty": random.randint(1,200),
    "Profit/Loss": profit + " of " + data1["Global Quote"]["09. change"],
    "Profit/Loss %": data1["Global Quote"]["10. change percent"]    
}]

table = tabulate(filtered_data, headers= "keys")

print(table)