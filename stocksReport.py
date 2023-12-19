"""Displays stock information based off of user input."""

from tabulate import tabulate
import random

symbol = input("Enter the stock symbol: ")
purchase = input("Enter the purchase date: ")
stockQty = input("Enter the quantity: ")
price = input("Enter the purchase price per stock: ")

data = [{
    "Stock": symbol,
    "Purchase Date": purchase,
    "Quatity": stockQty,
    "Purchase Price per Stock": price

}]

table = tabulate(data, headers="keys")

print(table)