import requests
from bs4 import BeautifulSoup
from .CrawledArticle import CrawledArticle
from urllib.parse import urljoin

class ArticleFetcher():
    def fetch(self, url):
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []
        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = urljoin(url, card.select_one("img").attrs["src"])

            yield CrawledArticle(title, emoji, content, image)