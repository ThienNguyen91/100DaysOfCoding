import smtplib as smtp
import datetime as dt
import pandas as pd
from random import choice
letter_list = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]
INPUT_DIR = "birthdays.csv"
current_time = dt.datetime.now()
day = current_time.day
month = current_time.month

user_email = "giathiennc006@gmail.com"
user_email_password = "fgky mlyx ddti axmu"

with open(INPUT_DIR) as birthday_file:
    birthday_data = pd.read_csv(birthday_file)
for index, row in birthday_data.iterrows():
    if day == row["day"] and month == row["month"]:
        with open(choice(letter_list), "r") as letter_file:
            letter_data = letter_file.read()
            letter_data = letter_data.replace("[NAME]", row["name"])
        with smtp.SMTP("smtp.gmail.com") as C_smtp:
            C_smtp.starttls()
            C_smtp.login(user=user_email, password=user_email_password)
            C_smtp.sendmail(from_addr=user_email, to_addrs=row["email"], msg=f"Subject: Happy Birthday\n\n {letter_data}")