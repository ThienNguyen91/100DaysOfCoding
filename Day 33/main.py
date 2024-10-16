import requests
from datetime import datetime
import smtplib
MY_LAT = 10.888847 # Your latitude
MY_LONG = 106.767842 # Your longitude
USER_EMAIL = "giathiennc006@gmail.com"
USER_PASSWORD = "fgky mlyx ddti axmu"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def login():
    C_smtp = smtplib.SMTP("smtp.gmail.com")
    C_smtp.starttls()
    C_smtp.login(user=USER_EMAIL, password=USER_PASSWORD)
    return C_smtp

#If the ISS is close to my current position
if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        sender = login()
        sender.sendmail(from_addr= USER_EMAIL, to_addrs="giathiennc123123@gmail.com", msg="Look up")

# BONUS: run the code every 60 seconds.



