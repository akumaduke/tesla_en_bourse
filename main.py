import requests
from twilio.rest import Client


NOM_STOCK = "TSLA"
NOM_KONPAYI = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
KLE_APi="cle_apiw"
KLE_API_NEWS= "cle_apiw"
twilio_sid="twilio_sid"
twilio_token="Twilio_token"



paramet_stock={
    "function": "TIME_SERIES_DAILY",
    "symbol": NOM_STOCK,
    "apikey": KLE_APi,

}
reponse= requests.get(STOCK_ENDPOINT,params= paramet_stock )
done=reponse.json()["Time Series (Daily)"]
lis_done= [valeur for (kle, valeur) in done.items()]
done_hier= lis_done[0]
pri_femen_hier= done_hier["4. close"]


done_avanye=lis_done[1]
pri_femen_avanye= done_avanye["4. close"]

difference= abs(float(pri_femen_hier)-float(pri_femen_avanye))

pousantaj= (difference/float(pri_femen_hier)) *100


if pousantaj>0.001:
    news_param={
        "apiKey":KLE_API_NEWS,
        "qInTitle":NOM_KONPAYI
    }
    nouvo_repons=requests.get(NEWS_ENDPOINT, params=news_param)
    article= nouvo_repons.json()["articles"]
    trois_articles= article[:3]
    print(trois_articles)

    nouvo_article=[f"Men nouvel action antrepriz wap suiv lan:{article['title'] } . \n resume:{article['description']}\n by AKUMA " for article in trois_articles]

    client=Client(twilio_sid, twilio_token)
    for article in nouvo_article:
        message= client.messages.create( body=article,from_= "twilio_number", to= "your_number" )


