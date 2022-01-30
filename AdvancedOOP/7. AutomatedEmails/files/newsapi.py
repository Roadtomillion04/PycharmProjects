# We are scrapping news from newsapi.org
# and the api key is 3f679802901e4e429b625a9f496d1cc9

import requests

url = "https://newsapi.org/v2/everything?" \
      "qInTitle=tesla&" \
      "from=2021-12-27&" \
      "to=2021-12-28&" \
      "language=en&" \
      "apiKey=3f679802901e4e429b625a9f496d1cc9"
# you can filter the results by changing values

res = requests.get(url= url)
# As we are getting raw data (json format) we can't filter using str like in HTML
content = res.json() # converts binary to json

# Now content is dict, Let's filter the content
    # articles key val= [] 1st  key inside list
title = content['articles'][0]['title']
link = content['articles'][0]['url']

print(title, link)

# Let's grab all the title and links
articles = content['articles']

email_body = ''
for article in articles:                                    # two new line
    email_body += article['title'] + '\n' + article['url'] + '\n\n'

print(email_body)
