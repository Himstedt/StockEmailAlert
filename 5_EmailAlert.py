import os
import smtplib
import imghdr
from email-message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()

yf.pdr_override()
start = input("Enter a start year: ")
startyear = int(startyearIn)
now = dt.datetime.now()

stock = input("Enter a stock ticker symol: ")
TargetPrice = input("What price do you want to trigger the alert: ")

msg["Subject"] = "Alert on"+stock
msg["From"] = EMAIL_ADDRESS
msg["To"] = "jon@doe.com"

alerted = False

while 1:
    df = pdr.get_data_yahoo(stock, start, now)
    currentClose = df["Adj Close"][-1]

    condition = currentClose > TargetPrice

    if(condition and alerted == False):

        alerted = True

        message = stock + " has activated the alert price off "+ str(TargetPrice) +\"\nCurrent Price: "+str(currentClose)

        msg.set_content(message)

        files = [r"C:\Users\Jon\Documents\Fundamental List.xlsx"]

        for file in files:
            with open(file, "rb") as f:
                file.data = f.read()
                file_name = "FundamentalList.xlsx"

                msg.add_attachment(file_data, maintype = "application",
                    subtype = 'ocetet-stream', filename = file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

            print("complet")

    else:
        print("no new alerts")


    time.sleep(300)
