import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "stock api key here"
NEWS_API_KEY = "news api key here"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_paramas = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,

}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_paramas)
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
day_bef_yesterday = data_list[1]
yesterday_closing = yesterday_data["4. close"]
day_bef_yesterday_closing = day_bef_yesterday["4. close"]
percent_change = round(abs((float(yesterday_closing) - float(day_bef_yesterday_closing))/float(yesterday_closing)*100))
if yesterday_closing > day_bef_yesterday_closing:
    up_or_down = "🔼"
else:
    up_or_down = "🔽"
if percent_change >= 4:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles_data = news_response.json()["articles"]
    three_articles = articles_data[:3]
    news_articles = [f"Heading: {article['title']} \n Brief: {article['description']}" for article in three_articles]
    account_sid = "accound sid here"
    auth_token = "auth token here"
    client = Client(account_sid, auth_token)
    for article in news_articles:
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {up_or_down}{percent_change}%{article}",
            from_='sender s number here',
            to='receiver s number here',
        )
    print("Messages are being sent.")

