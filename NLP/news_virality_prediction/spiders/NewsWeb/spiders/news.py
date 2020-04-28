import scrapy

# Scrapy uses Request and Response objects for crawling web sites.
from scrapy.http import Request

from NewsWeb.items import NewswebItem

class news(scrapy.Spider):
    # name should be same as spider name
    # name should be lower case
    name = "news"
    page_number = 1
    # start_urls not start_url
    # put inside []
    start_urls = ['https://theprint.in/category/india/']


    def parse(self, response):

        item = NewswebItem()
        #
        # source_code = response.css("div.view view-category-wise-content-list")



        # content = response.xpath('/html/body/div[6]/div[4]/div/div/div[1]')


        # copy paste fromm chrome
    #td-outer-wrap > div.td-main-content-wrap.td-container-wrap > div > div > div.td-pb-span8.td-main-content

        source_code = response.css("div.td-pb-span8.td-main-content")
        for link in source_code:

            title_link = link.css("div.td-module-thumb a::attr(href)").extract()

        # creating item container

            item['title_link'] = title_link

        yield item
        # return items2

        next_page = 'https://theprint.in/category/india/page/'+str(news.page_number)+'/'

        if news.page_number <= 300:

            news.page_number = news.page_number + 1

            yield response.follow(next_page, callback = self.parse)


















