import smtplib as smtp
import datetime as dt
import pandas as pd
letter_list = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]
INPUT_DIR = "birthdays.csv"


user_email = "giathiennc006@gmail.com"
user_email_password = "fgky mlyx ddti axmu"

C_smtp = smtp.SMTP("smtp.gmail.com")
C_smtp.starttls()
C_smtp.login(user=user_email, password=user_email_password)
with open(INPUT_DIR) as birthday_file:
    birthday_data = pd.readcsv(birthday_file)
