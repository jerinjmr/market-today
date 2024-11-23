"""Stock recommendation system.

Python web scraping technology is used to extract information from website.
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from functools import lru_cache
from typing import List, Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add request timeout and headers
TIMEOUT = 10
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def fetch_url(url: str) -> str:
    """Fetch URL with error handling."""
    try:
        response = requests.get(url, timeout=TIMEOUT, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return ""

def get_stock_reco() -> List[Tuple[str, str, str]]:
    """Fetch stock recommendations with parallel requests."""
    urls = [
        'https://www.moneycontrol.com/news/business/stocks/',
        'https://www.moneycontrol.com/news/business/stocks/page-2',
        'https://economictimes.indiatimes.com/markets/stocks/recos'
    ]
    
    # Parallel fetch of URLs
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        responses = list(executor.map(fetch_url, urls))
    
    soups = [BeautifulSoup(resp, 'html.parser') for resp in responses if resp]
    
    link1 = soups[0].select('#cagetory')
    link2 = soups[1].select('#cagetory')
    links = link1 + link2
    link3 = soups[2].select('.eachStory')

    def fetch_market_news_01(links):
        """Fetch market feeds."""
        news = []
        for item in links:
            level1 = item.select('.clearfix')
            for element in level1:
                level2 = element.a
                title = level2.get('title')  # Gets the title
                url = level2.get('href')
                date_comment = element.find(string=lambda text: isinstance(text, str) and 'IST' in text)
                date_text = date_comment.strip('<!-- <span>').strip()
                date = datetime.strptime(date_text[:-6], '%B %d, %Y %I:%M %p')
                subject = [date, title, url]
                news.append(subject)
        return news

    def fetch_market_news_02(links):
        news = []
        url = "https://economictimes.indiatimes.com/"
        for item in links:
            level3 = item.time
            date = level3.getText()
            date = datetime.strptime(date[:-4], '%b %d, %Y, %I:%M %p')
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


if __name__ == '__main__':
    print(get_stock_reco())
