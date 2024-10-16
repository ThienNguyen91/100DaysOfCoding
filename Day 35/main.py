import requests as rq
from twilio.rest import Client

account_sid = "ACf64ccf9e64e591b40b76857dbf38d633"
auth_token = "5214e6628bca5f57ee72b77928fa6076"
TWILIO_PHONE = "whatsapp:+14155238886"
USER_PHONE = "whatsapp:+84763811806"
client = Client(account_sid, auth_token)




parameters = {
    "lat":10.888831,
    "lon":106.768102,
    "appid": "f89bc28c676221f5fe59c8f1ba60da8c",
    "cnt":4,
}
#Call weather API
weather_api = rq.get(url= "https://api.openweathermap.org/data/2.5/forecast", params= parameters)
weather_api.raise_for_status()
weather_data = weather_api.json()

#Check will it rain next 12 hours
will_rain = False
for i in range(4):
    weather_id = weather_data["list"][i]["weather"][0]["id"]
    #Weather will rain
    if weather_id < 700:
        will_rain = True
        break

if will_rain:
    # Build message for weather forecast
    message_lines = ["It's going to rain tomorrow. Remember to bring an ☂️\n"]
    for index, each_hour in enumerate(weather_data["list"]):
        #Reached out of next 12 hours
        if index> 3:
            break
        weather_desc = each_hour["weather"][0]["description"]
        day_time = each_hour["dt_txt"]
        message_lines.append(f"The weather will be {weather_desc} at {day_time}\n")

    #send message to user via WhatsApp
    my_msg = ''.join(message_lines)
    message = client.messages.create(
        body=my_msg,
        from_=TWILIO_PHONE,
        to=USER_PHONE,
    )
    print(message.status)