import crawler

super_fetcher = crawler.WholeSiteCrawler()
art = super_fetcher.crawl()
for a in art:
    print(a.title)