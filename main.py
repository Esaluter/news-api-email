import requests

api_key = "70b766f12e554e58a3efacb67ce28ed6"
url = "https://newsapi.org/v2/everything?"\
        "q=tesla&from=2023-10-28&sortBy=publishe"\
        "dAt&apiKey=70b766f12e554e58a3efacb67ce28ed6"

#make request
request = requests.get(url)

#make a dictionary with data
content = request.json()

#acces article title and descriptions
for article in content['articles']:
    print(article["title"])
    print(article["description"])
