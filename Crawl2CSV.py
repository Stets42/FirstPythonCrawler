import crawler
import csv

crawler = crawler.WholeSiteCrawler()
articles = crawler.crawl()

with open('crawledArticles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Title", "Emoji", "Content", "Image"])
    for article in articles:
        writer.writerow([article.title, article.emoji, article.content, article.image])