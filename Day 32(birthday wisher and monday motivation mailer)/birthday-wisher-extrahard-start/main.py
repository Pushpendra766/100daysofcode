##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
from random import randint
PLACEHOLDER = "[NAME]"
my_email = "example@gmail.com"
my_pass = "ashduf79asdfgasd@"

now = dt.datetime.now()
today_tuple = (now.month, now.day)
dob_data = pandas.read_csv("birthdays.csv")
dob_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in dob_data.iterrows()}
if today_tuple in dob_dict:
    birthday_boy = dob_dict[today_tuple]
    letter_number = randint(1, 3)
    friend_email = birthday_boy["email"]
    with open(f"letter_templates/letter_{letter_number}.txt") as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace(PLACEHOLDER, birthday_boy["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=friend_email,
            msg=f"Subject:Happy Birthday\n\n{new_letter}"
        )







