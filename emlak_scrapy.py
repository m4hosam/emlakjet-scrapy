import scrapy
import json


#  scrapy runspider emlak_scrapy.py

class EmlakJetSpider(scrapy.Spider):
    name = 'emlakjet'
    start_urls = ['https://www.emlakjet.com/satilik-konut/kocaeli/{}/'.format(i) for i in range(1, 2)]
    ev_links = []
    ev_detaylar = []
    def parse(self, response):
        # Extracting links with class "_3qUI9q"
        property_links = response.css('a._3qUI9q::attr(href)').getall()
        # Visiting each property link
        for link in property_links:
            # EmlakJetSpider.ev_links.append(link)
            yield response.follow(
                link, callback=self.parse_ev_detay)
            # yield scrapy.Request(response.urljoin(link), callback=self.parse_property)

    def parse_ev_detay(self, response):
        # Extracting details from class "_35T4WV"
        details = response.css('div._35T4WV div._1bVOdb::text').extract()
        details = [detail.strip() for detail in details if detail.strip()]
        details_dict = {details[i]: details[i+1] for i in range(0, len(details), 2)}

        # Extracting price
        price = response.css('div._2TxNQv::text').extract_first().strip()

        # EmlakJetSpider.ev_links.append(price)
        details_dict['url'] = response.url
        details_dict['price'] = price
        EmlakJetSpider.ev_detaylar.append(details_dict)
        yield details_dict

    def closed(self, reason):
        """
        This method is called when the spider is closed.
        Save the products to JSON file here.
        """
        with open("evler.json", "w", encoding='UTF-8') as file:
            json.dump(EmlakJetSpider.ev_detaylar, file, ensure_ascii=False)

