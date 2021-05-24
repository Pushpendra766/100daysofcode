import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
PRODUCT_URL = "https://www.amazon.in/Camel-Oil-Pastel-Reusable-Plastic/dp/B00LY12TH6/ref=sr_1_1?dchild=1&keywords=oil+pastels&qid=1621483789&sr=8-1"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT,
}
response = requests.get(url=PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
price_string = (soup.find(name="span", class_="priceBlockStrikePriceString")).string
price_string.encode('utf-8')
price = float(price_string.split()[1])
product = (soup.find(name="span", class_="a-size-large product-title-word-break")).string
product_name = " ".join(product.split())
user_name = YOUR_EMAIL
password = YOUR_PASSWORD
message=f"{product_name} is now Rupees {price}\n{PRODUCT_URL}"
print(message)
if price < 250:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_name, password=password)
        connection.sendmail(
            from_addr=user_name,
            to_addrs= TO_EMAIL ,
            msg=f"Subject:Low Price Alert\n\n{message}"
        )
    print("Sent")