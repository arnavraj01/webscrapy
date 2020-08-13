import scrapy
from datetime import date
import pandas as pd

class ArticleSpider(scrapy.Spider):
    name = "articles"
    def __init__(self):
        articles_df = pd.read_json('dump1308.json')
        articles_df.head()
        urls = [a for a in articles_df.link.unique()]
        # urls = ['https://www.thehindu.com/news/national/ramvilas-paswan-asks-states-to-do-doorstep-ration-delivery-in-flood-hit-areas/article32326564.ece']
        self.start_urls = urls

    def parse(self,response):
        yield {
            'publishdate': response.xpath("//meta[@name='publish-date']/@content")[0].extract(),
            'createddate': response.xpath("//meta[@name='created-date']/@content")[0].extract(),
            'modifieddate': response.xpath("//meta[@name='modified-date']/@content")[0].extract(),
            'section': response.xpath("//meta[@property='article:section']/@content")[0].extract(),
            'author': response.xpath("//meta[@property='article:author']/@content")[0].extract(),
            'tags': response.xpath("//meta[@property='article:tag']/@content").getall(),
            'title': response.xpath("//meta[@name='title']/@content")[0].extract(),
            'description': response.xpath("//meta[@name='description']/@content")[0].extract(),
            'text': '\n'.join(response.css('div.paywall p::text').getall()),
            'url':response.url,
            'hash': hash('\n'.join(response.css('div.paywall p::text').getall()))
        }

                                            # <div id="content-body-14269002-32326564" class="paywall">
                                            #     <p>Union Food Minister Ramvilas Paswan has appealed to the State governments to carry out doorstep delivery of ration to those eligible under the National Food Security Act (NFSA) and the Pradhan Mantri Garib
                                            #         Kalyan Anna Yojana in flood-affected areas. </p>
                                            #     <p>“Floods and heavy rains in many states of the country have resulted in catastrophic conditions. People are leaving the village and taking shelter elsewhere and it is not possible for people to reach the
                                            #         ration shops,” he said in a series of tweets. </p>
                                            #     <p>Parts of Bihar, Kerala, Karnataka, Assam and other northeastern States have been affected by severe flooding. </p>
                                            #     <p>“I urge the State Governments to arrange Door-Step Delivery of ration for those who are not able to get ration from the ration shop under the flood affected National Food Security Act and the Pradhan Mantri
                                            #         Garib Kalyan Anna Yojana,” Mr Paswan said. He stressed that timely distribution of grains at the time of calamity became even more critical and the State governments have to step in in this hour of crisis.
                                            #         </p>
                                            #     <p>Through the Pradhan Mantri Garib Kalyan Anna Yojana and the National Food Security Act, the Central government is giving 10 kg of food grains a month to more than 80 crore beneficiaries of NFSA from April
                                            #         to November. This, the Ministry estimates in case of a family of four amounts to three quintals in 8-months. </p>
                                            # </div>



    # <meta property="article:author" content="Special Correspondent" />
    # <meta property="article:tag" content="flood-hit States" />
    # <meta property="article:tag" content="ration at doorsteps" />
    # <meta property="article:tag" content="Ramvilas Paswan" />
    # <meta property="article:tag" content="Ramvilas Paswan for ration items at doorsteps by States" />
    # <meta property="article:tag" content="ration delivery at doorstep" />
    # <meta property="article:tag" content="delivery of ration" />
    # <meta property="article:section" content="National" />
    # <meta name="publish-date" content="2020-08-11T17:55:12+05:30" />
    # <meta name="created-date" content="2020-08-11T17:55:12+05:30" />
    # <meta name="modified-date" content="2020-08-11T17:55:12+05:30" />