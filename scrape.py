"""Stock recommendation system.

Python web scraping technology is used to extract information from website.
"""
import requests
from bs4 import BeautifulSoup


def get_stock_reco():
    """
    Scrape stock news from moneycontrol.

    Extracts date and new titles.

    :return market_news: list of tuples of date and title.
    """
    res1 = requests.get('https://www.moneycontrol.com/news/business/stocks/')
    res2 = requests.get(
        'https://www.moneycontrol.com/news/business/stocks/page-2')

    soup1 = BeautifulSoup(res1.text, 'html.parser')
    soup2 = BeautifulSoup(res2.text, 'html.parser')

    link1 = soup1.select('#cagetory')
    link2 = soup2.select('#cagetory')
    links = link1 + link2

    def fetch_market_news(links):
        """Fetch market feeds."""
        news = []
        for item in links:
            level1 = item.select('.clearfix')
            for element in level1:
                level2 = element.a
                title = level2.get('title')  # Gets the title
                level3 = element.span
                date = level3.getText()  # Gets the date and time
                subject = (date, title)
                news.append(subject)
        return news

    market_news = fetch_market_news(links)
    return market_news
