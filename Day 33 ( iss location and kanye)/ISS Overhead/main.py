import requests
from datetime import datetime
import smtplib
import time

MY_LONGITUDE = [enter you longitude here]
MY_LATITUDE = [enter you latitude here]
USER = "sender email here"
PASS = "sender password here"

parameters = {
        "lng": MY_LONGITUDE,
        "lat": MY_LATITUDE,
        "formatted": 0
    }
response_time = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
time_data = response_time.json()
sunrise = int(time_data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(time_data['results']['sunset'].split('T')[1].split(':')[0])


def is_night():
    time_now = datetime.now().hour - 5
    if (sunset < time_now < 24) or (0 < time_now < sunrise):
        return True


def iss_in_range():
    response_loc = requests.get(url="http://api.open-notify.org/iss-now.json")
    loc_data = response_loc.json()
    latitude = float(loc_data['iss_position']['latitude'])
    longitude = float(loc_data['iss_position']['longitude'])
    # longitude = 79
    # latitude = 20
    long_min = longitude-5
    long_max = longitude+5
    lat_min = latitude-5
    lat_max = latitude+5
    print(f"Longitude = {long_min} : {MY_LONGITUDE} : {long_max}")
    print(f"Latitude = {lat_min} : {MY_LATITUDE} : {lat_max}")
    if long_min<MY_LONGITUDE<long_max and lat_min<MY_LATITUDE<lat_max:
        return True


def send_email():
    with smtplib.SMTP("your email provider's smtp address here") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASS)
        connection.sendmail(
            from_addr=USER,
            to_addrs=PASS, # sending email to self
            msg="Subject:ISS in your location\n\nLook up the sky."
        )


while True:
    time.sleep(60) # refreshes every 60 seconds
    if is_night():
        print("It is night")
        iss_loc = iss_in_range()
        if iss_loc:
            print("ISS is in your location")
            send_email()
            print("Mail sent.")
