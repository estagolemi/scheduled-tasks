
import datetime as dt
import smtplib
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote_of_the_week = random.choice(quotes)
    print(quote_of_the_week)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivational Quote\n\n {quote_of_the_week}"
        )


