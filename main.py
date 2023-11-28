import requests
from send_email import send_email

api_key = "70b766f12e554e58a3efacb67ce28ed6"
url = "https://newsapi.org/v2/everything?"\
        "q=tesla&from=2023-10-28&sortBy=publishe"\
        "dAt&apiKey=70b766f12e554e58a3efacb67ce28ed6"

#make request
request = requests.get(url)

#make a dictionary with data
content = request.json()

#acces article title and descriptions
body = ''
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"
    #print(article["title"])
    #print(article["description"])
        #message = f'Привет! Лови немного новостей {article["title"]} {article["description"]}'  

body = body.encode("UTF-8")
send_email(body)