import time
import yagmail
import pandas as pd
from news_feed import NewsFeed
from datetime import datetime

def send_today_news():
    df = pd.read_excel(io='files/people.xlsx')

    for idx, row in df.iterrows():
        news = NewsFeed(interest=row.interest)
                                # make sure less secure apps is on
        email = yagmail.SMTP(user='karurnirmal04@gmail.com',
                             password='13032004')

        email.send(to=row.email,  # for some reason row.name returns idx
                   subject=f'Hi there... {row["name"]}, we got news on {row.interest} today!!',
                   contents=f'Checkout the hottest news on {row.interest}, '
                            f'\n\n {news.get_news()} \n -God')


if __name__ == "__main__":
    while True:    # datetime follows international clock 0 - 23
        if datetime.now().hour == 5 and datetime.now().minute == 30:
            send_today_news()
        time.sleep(secs= 60) # executes only once

