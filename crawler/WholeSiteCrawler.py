import requests
from bs4 import BeautifulSoup
from .ArticleFetcher import ArticleFetcher
from urllib.parse import urljoin

class WholeSiteCrawler():
    def crawl(self):
        r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
        doc = BeautifulSoup(r.text, "html.parser")

        page_count = int(doc.select("p")[1].text.split()[3])

        button_link_first_part = doc.select_one(".btn").attrs["href"].split("=")[0]

        fetcher = ArticleFetcher()
        all_articles = []
        counter = 1
        while counter <= page_count:
            page_url = button_link_first_part + "=" + str(counter)
            current_url = urljoin("http://python.beispiel.programmierenlernen.io/index.php", page_url)
            for art in fetcher.fetch(current_url):
                all_articles.append(art)
            counter = counter + 1
        return all_articles