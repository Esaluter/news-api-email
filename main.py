import requests
from send_email import send_email

api_key = "70b766f12e554e58a3efacb67ce28ed6"
url = "https://newsapi.org/v2/everything?"\
    "q=tesla&"\
    "from=2023-11-01&" \
    "sortBy=publishedAt&"\
    "apiKey=70b766f12e554e58a3efacb67ce28ed6&"\
    "language=ru"

#make request
request = requests.get(url)

#make a dictionary with data
content = request.json()

#acces article title and descriptions
body = ''
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
        + article["description"] \
        + "\n" + article["url"] + 2*"\n" 
      #"Subject: Новости" + "\n"  + 

body = body.encode("UTF-8")
send_email(body)