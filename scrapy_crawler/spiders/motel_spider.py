import scrapy
from scrapy_crawler.items import ScrapyCrawlerMotel
import json
class MotelSpider(scrapy.Spider):
    name='motel'
    allowed_domains=['phongtro123.com']
    # find motels in HCM
    start_urls=['https://phongtro123.com/tinh-thanh/ho-chi-minh']
    
    def parse(self, response):
        district_links=response.css('ul.row.gx-0 a::attr(href)').getall()
        
        for link in district_links:
            yield response.follow(link,callback=self.parse_district)
    
    def parse_district(self, response):
        posts=response.css('ul.post__listing li')
        for post in posts:
            item=ScrapyCrawlerMotel()
            item['title']=post.css('h3 a::attr(title)').get()
            area_text=post.xpath('.//div[contains(@class,"mb-2 line-clamp-1")]/span[contains(text(),"m")]//text()').getall()
            if area_text:
                item['area']=" ".join([text.strip() for text in area_text if text.strip()])
            script_text=post.css('script[type="application/ld+json"]::text').get()
            if script_text:
                data=json.loads(script_text)
                item['price']=data['priceRange']
                item['description']=data['description']
                item['address']=data['address'].get('streetAddress')
                item['url']=data['url']
                item['telephone']=data.get('telephone')
                
                yield response.follow(item['url'],callback=self.parse_area_description,cb_kwargs={'item':item})
                
        next_page=response.css('ul.pagination a[rel="next"]::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse_district)
            
    def parse_area_description(self,response,item):
        html_desc_pieces=response.xpath('//h2[contains(text(),"Thông tin mô tả")]/following-sibling::p//text()').getall()
        if html_desc_pieces:
            full_decs=" ".join([text.strip() for text in html_desc_pieces if text.strip()])
            item['description']=full_decs
        yield item