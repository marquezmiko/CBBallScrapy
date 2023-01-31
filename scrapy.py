import scrapy

class CBBallSpider(scrapy.Spider):
    name = 'Cbball_spider'
    start_urls = ['https://www.reddit.com/r/CollegeBasketball/comments/10p7u9m/ap_poll_week_13/']


    def parse(self, response):
        pList = []
        for div in response.xpath('//div[@data-testid="comment"]'):
            text = div.css("p::text").extract_first()
            pList.append(text)
            # yield {
            #     'p': text
            # }
        print(pList)



# >>> response.xpath('//h1/text()')
# [<Selector xpath='//h1/text()' data='Userpoll: Week 13'>]
# >>> response.xpath('//div[contains(.,"Comment")]').getall()
# >>> response.xpath('//div[@data-testid="comment"]')
