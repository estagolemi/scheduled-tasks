
import datetime as dt
import smtplib
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        quote_of_the_week = random.choice(quotes)
    print(quote_of_the_week)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Monday Motivational Quote\n\n {quote_of_the_week}"
        )


