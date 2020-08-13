https://docs.scrapy.org/en/latest/intro/tutorial.html

scrapy startproject webscrappy     # Create Scrapppy Project

scrapy crawl hindunews   # run your crawler
scrapy shell 'http://quotes.toscrape.com/page/1/'   # Use In line Scrappy
scrapy crawl hindunews -o news.json  # to crawl hindunews and store in news.json
