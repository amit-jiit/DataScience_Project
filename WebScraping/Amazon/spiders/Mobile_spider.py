import scrapy

from Amazon.items import mobile_item



# class should be same as spider name
class Mobile_spider(scrapy.Spider):
    # name should be same as spider name
    name = "Mobile_spider"
    page_number = 2
    # Page 1 of 110
    start_urls = [
        'https://www.flipkart.com/search?q=new+release+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.price_range.from%3D7000&p%5B%5D=facets.price_range.to%3D30000']

    def parse(self, response):

        items = mobile_item()

        # using selector gadget find css selector code
        # to get text from css selector
        phone_name = response.css("div._3wU53n::text").extract()
        # multiple class object
        phone_price = response.css("div._1vC4OE _2rQ-NK::text").extract()
        phone_rating = response.css(".hGSR34::text").extract()
        percent_off = response.css(".VGWI6T span::text").extract()

        # creating temporary item container

        items['smartphone_name'] = phone_name
        items['smartphone_price'] = phone_price
        items['smartphone_rating'] = phone_rating
        items['percentage_off'] = percent_off

        yield items

        next_page = 'https://www.flipkart.com/search?q=new+release+mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&p%5B%5D=facets.price_range.from%3D7000&p%5B%5D=facets.price_range.to%3D30000&page='+str(Mobile_spider.page_number)+'/'
        # Showing 1 – 24 of 2,617 results for "new release mobile"
        # new release smartphone with price range 7k to 30k in india on flipkart
        # Page 1 of 110
        if Mobile_spider.page_number <= 110:

            Mobile_spider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
















