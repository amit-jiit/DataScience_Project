
import scrapy
import json
# from scrapy.http import Request
from NewsWeb.items import NewswebItem

from scrapy import Request


class news_article(scrapy.Spider):

    name = 'news_article'
    start_urls = ['https://theprint.in/category/india/']


    def start_requests(self):
        # open csv file
        with open('csvjson.json') as json_file:
            data = json.load(json_file)

            for p in data:
                url = p['title_link']

    # Request to get the HTML content
                # request = Request(url,callback=self.parse_article)
                request = Request(url, callback=self.parse_article)
                yield request

    def parse_article(self,response):

        item = NewswebItem()
        title = response.css("h1.entry-title::text").extract()
        summary = response.css("h2.td-post-sub-title::text").extract()

        author = response.css(".fn::text").extract()
        # "" should not repeat
        like_facebook = response.xpath('//*[@id="u_0_2"]').get()
        # // *[ @ id = "u_0_2"] copy from chrome xpath
        # like_facebook = response.css("iframe::text").extract()

        tags = response.xpath('//ul["td-tags td-post-small-box clearfix"]/li/a/text()').getall()
        # // *[ @ id = "post-408287"] / div[2] / div[1] / div / footer / div[1] / ul / li[3] / a
        # // *[ @ id = "post-408287"] / div[2] / div[1] / div / footer / div[1] / ul / li[4] / a
        # // *[ @ id = "post-408287"] / div[2] / div[1] / div / footer / div[1] / ul / li[1] / span
        date = response.css("span.update_date::text").extract()

        item['title'] = title
        item['summary'] = summary
        item['author'] = author
        item['like_facebook'] = like_facebook
        item['tags'] = tags
        item['date'] = date

        yield item









