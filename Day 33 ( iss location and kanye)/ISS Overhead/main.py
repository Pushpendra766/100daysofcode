import requests
from datetime import datetime
import smtplib

MY_LONGITUDE = 76.401588
MY_LATITUDE = 23.640445
# USER = "codestrong7@yahoo.com"
# PASS = "gioteyrpfxeowdcq"

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
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user="codestrong7@yahoo.com", password="gioteyrpfxeowdcq")
        connection.sendmail(
            from_addr="codestrong7@yahoo.com",
            to_addrs="codestrong7@gmail.com",
            msg="Subject:ISS in your location\n\nLook up the sky."
        )


while True:
    if is_night():
        print("It is night")
        iss_loc = iss_in_range()
        if iss_loc:
            print("ISS is in your location")
            send_email()
            print("Mail sent.")
