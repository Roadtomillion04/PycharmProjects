import requests
import datetime

class NewsFeed:
    """Represents title and links of the user giving data in single string for email body
    """
    static_url:str = "https://newsapi.org/v2/everything?"

    api_key:str = "3f679802901e4e429b625a9f496d1cc9"

    def __init__(self, interest,
                 # subtract 1 day
                 from_date= datetime.date.today() - datetime.timedelta(days=1),
                 to_date= datetime.date.today(),
                 language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def _build_url(self):
        url = f"{self.static_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url

    def _get_articles(self, url):
        # scrapping news data
        res = requests.get(url=url)
        content = res.json()
        articles = content['articles']
        return articles

    def get_news(self):
        url = self._build_url()
        articles = self._get_articles(url)

        # filter news data (title&url)
        email_body:str = ''
        for article in articles:
            email_body += article['title'] + '\n' + article['url'] + '\n\n'
        return email_body


if __name__ == "__main__": # to run only when on executed not imported
    news_feed = NewsFeed(interest= 'gaming', language='en')
    print(news_feed.get_news())
