import requests
from twilio.rest import Client

STOCK_NAME = "RELIANCE.BSE"
COMPANY_NAME = "RELIANCE"

account_sid = "ACcba6c9e16617f091ca4c9706911732f3"
auth_token = "3e152182161e05fb79f3f88e65d77609"
api_key = "TT96XO0216DYJLV5"
news_Api = "bccd79d1c77f49248534900f5b281c0b"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : api_key,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
print(yesterday_closing)

day_before_yesterday = data_list[1]
day_before_yesterday_closing = day_before_yesterday["4. close"]
print(day_before_yesterday_closing)

difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
print(difference)

diff_percent = (difference/float(yesterday_closing)) * 100
print(diff_percent)

if diff_percent > 0.1:
    news_params = {
        "apiKey" : news_Api,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    three_Articles = articles[:3]
    print(three_Articles)

    formatted_articles = [f"Headline : {article['title']}. \nBrief: {article['description']}" for article in three_Articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_= "+15732451969",
            to="+919354034429",)



