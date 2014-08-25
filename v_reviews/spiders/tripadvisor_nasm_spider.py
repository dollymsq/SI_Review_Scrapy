import scrapy
from scrapy.selector import Selector
from v_reviews.items import VReviewsItem


class DmozSpider(scrapy.Spider):
    name = "tripadvisor_nasm"
    allowed_domains = ["tripadvisor.com"]
    base_uri = "http://www.traipadvisor.com"
    start_urls = [
#         base_uri+"/ShowUserReviews-g28970-d107967-r223827433-Smithsonian_National_Air_and_Space_Museum-Washington_DC_District_of_Columbia.html#REVIEWS"
        "http://www.tripadvisor.com/Attraction_Review-g28970-d107967-Reviews-Smithsonian_National_Air_and_Space_Museum-Washington_DC_District_of_Columbia.html"
        ]
        

    def parse(self, response):
        filename = "tripadvisor_nasm"
        with open(filename, 'wb') as f:
            f.write(response.body)
        
        sel = Selector(response)
        divs = sel.css('.basic_review')
        for sel in divs:
            username = sel.css('.username span::text').extract()
            date = sel.css('.ratingDate::text').extract()
            rate = sel.css('.sprite-rating_s_fill').xpath('@alt').extract()
            content = sel.css('.partial_entry::text').extract()
            link = sel.css('.quote a').xpath('@href').extract()
#             print "%s\n%s\n%s\n%s\n%s\n"  % (username, date, rate, content, link)
            
            item = VReviewsItem()
            item['username'] = username
            item['date'] = date
            item['rate'] = rate
            item['content'] = content
            item['link'] = link
            item['museum'] = "nasm"
            yield item