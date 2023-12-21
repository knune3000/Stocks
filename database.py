import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="db4free.net",
    user="knuser",
    password="knpassword1",
    database="coursedatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Stock_Positions (id, ticker, qty, purchase_date, purchase_price) VALUES (%s, %s, %s, %s, %s)"

user_id = int(input("Enter the stock id: "))
user_ticker = str(input("Enter the ticker: "))
user_qty = int(input("Enter the quantity of the stock: "))
user_date = input("Enter the date of the purchase in form (YYYY-MO-DA): ")
user_price = float(input("Enter the purchase price of the stock: "))

val = (user_id, user_ticker, user_qty, user_date, user_price)

mycursor.execute(sql, val)

mydb.commit()