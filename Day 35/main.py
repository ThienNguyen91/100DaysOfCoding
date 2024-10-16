import requests as rq
from twilio.rest import Client

account_sid = "ACf64ccf9e64e591b40b76857dbf38d633"
auth_token = "5214e6628bca5f57ee72b77928fa6076"
TWILIO_KEY = "SK7de823dd0d97b4c06486ce17de41394b"
TWILIO_PHONE = "+18507417533"
client = Client(account_sid, auth_token)




parameters = {
    "lat":10.888831,
    "lon":106.768102,
    "appid": "f89bc28c676221f5fe59c8f1ba60da8c",
    "cnt":4,
}
weather_api = rq.get(url= "https://api.openweathermap.org/data/2.5/forecast", params= parameters)
weather_api.raise_for_status()
weather_data = weather_api.json()
will_rain = False
for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        break
if will_rain:
    message = client.messages.create(
        body="It's going to rain tomorrow. Remember to bring an ☂️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+84763811806",
    )
    print(message.status)