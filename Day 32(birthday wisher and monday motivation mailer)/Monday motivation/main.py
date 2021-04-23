mimport random
import datetime as td
import smtplib
now = td.datetime.now()
weekday = now.date()
if weekday == 4:
    with open("quotes.txt") as file:
        moti_msg = file.readlines()
        message = random.choice(moti_msg)
        print(message)

        user_name = "example@gmail.com"
        password = "ajoifh67asha8"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user_name, password=password)

            connection.sendmail(
                from_addr=user_name,
                to_addrs="example@yahoo.com",
                msg=f"Subject:Motivation\n\n{message}"
            )

