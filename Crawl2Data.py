import crawler

crawler = crawler.WholeSiteCrawler()
articles = crawler.crawl()
for article in articles:
    print(article.title)
    print(str(len(articles)))