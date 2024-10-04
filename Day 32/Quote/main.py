import smtplib as smtp
import datetime as dt
from random import choice

user_email = "giathiennc006@gmail.com"
user_email_password = "fgky mlyx ddti axmu"
INPUT_DIR = "quote.txt"

C_smtp = smtp.SMTP("smtp.gmail.com")
C_smtp.starttls()
C_smtp.login(user=user_email, password=user_email_password)
with open(INPUT_DIR) as txt:
    quote_data = txt.readlines()
if dt.datetime.now().weekday() == 4:
    print("Birthday detected")
    C_smtp.sendmail(from_addr=user_email, to_addrs="giathiennc123123@gmail.com", msg=f"Subject: Friday quote\n\n{choice(quote_data)}")

