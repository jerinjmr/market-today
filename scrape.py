"""Stock recommendation system.

Python web scraping technology is used to extract information from website.
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_stock_reco():
    """
    Scrape stock news from moneycontrol.

    Extracts date and new titles.

    :return market_news: list of tuples of date and title.
    """
    res1 = requests.get('https://www.moneycontrol.com/news/business/stocks/')
    res2 = requests.get(
        'https://www.moneycontrol.com/news/business/stocks/page-2')

    res3 = requests.get(
        'https://economictimes.indiatimes.com/markets/stocks/recos')

    soup1 = BeautifulSoup(res1.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')
    soup3 = BeautifulSoup(res3.text, 'html.parser')

    link1 = soup1.select('#cagetory')
    link2 = soup2.select('#cagetory')
    links = link1 + link2
    link3 = soup3.select('.eachStory')

    def fetch_market_news_01(links):
        """Fetch market feeds."""
        news = []
        for item in links:
            level1 = item.select('.clearfix')
            for element in level1:
                level2 = element.a
                title = level2.get('title')  # Gets the title
                url = level2.get('href')
                level3 = element.span
                date = level3.getText()  # Gets the date and time
                date = datetime.strptime(date, '%B %d, %Y %I:%M %p %Z')
                subject = [date, title, url]
                news.append(subject)
        return news

    def fetch_market_news_02(links):
        news = []
        url = "https://economictimes.indiatimes.com/"
        for item in links:
            level3 = item.time
            date = level3.getText()
            date = datetime.strptime(date, '%b %d, %Y, %I:%M %p %Z')
            level1 = item.h3
            for element in level1:
                title = element.getText()  # Gets the title
                url = url + element.get('href')
            subject = [date, title, url]
            news.append(subject)
        return news

    market_news_01 = fetch_market_news_01(links)
    market_news_02 = fetch_market_news_02(link3)
    market_news = market_news_01 + market_news_02
    market_news.sort(reverse=True, key=lambda x: x[0])
    for item in market_news:
        item[0] = item[0].strftime('%B %d, %Y %I:%M %p')
    return market_news
