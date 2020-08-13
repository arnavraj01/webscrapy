import scrapy
from datetime import date


class NewsSpider(scrapy.Spider):
    name = "hindunews"
    def __init__(self):
        base = 'https://www.thehindu.com/news/'
        regions = ['national','international']
        states = ['andhra-pradesh', 'karnataka', 'kerala', 'tamil-nadu', 'telangana', 'other-states']
        cities = ['bangalore', 'chennai', 'Coimbatore', 'Delhi', 'Hyderabad', 'Kochi', 'kolkata']
        pages = range(0,14)
        urls = [base+region + '/?page=' + str(p)  for region in regions for p in pages]
        urls.extend([base + '/national/' + state +'/?page=' + str(p)  for state in states for p in pages])
        urls.extend([base+'/cities/'+city+'/?page='+str(p)  for city in cities for p in pages])
        self.start_urls = urls

    def parse(self,response):
        page = response.url.split("=")[-1]
        region = response.url.split("/")[-2]
        for cardnews in response.css("div.story-card-news"):
            yield {
                'extractedDate': date.today(),
                'headline': cardnews.css("h2 a::text,h3 a::text").get(),
                'link': cardnews.css("a::attr(href)").extract()[-1],
                'page': int(page),
                'region': region,
                'source': 'TheHindu',
                'hash':hash(cardnews.css("a::attr(href)").extract()[-1])
            }
        for cardnews in response.css("div.Other-StoryCard"):
            yield {
                'extractedDate': date.today(),
                'headline': cardnews.css("h2 a::text,h3 a::text").get(),
                'link': cardnews.css("a::attr(href)").extract()[-1],
                'page': int(page),
                'region': region,
                'source': 'TheHindu',
                'hash': hash(cardnews.css("a::attr(href)").extract()[-1])
            }