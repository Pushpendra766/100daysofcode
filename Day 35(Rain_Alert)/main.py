import requests
from twilio.rest import Client
api_key = "your api key here"
account_sid = "your account sid here"
auth_token = "your auth token here"
weather_params = {
    "lat":  37,
    "lon": 161,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    print(hour_data["weather"][0]["id"])
    if (hour_data["weather"][0]["id"]) < 700:
        will_rain = True
        break
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It will going to rain today.Don't forget to take ☂",
        from_='from number here',
        to='to number here',
    )
    print(message.status)