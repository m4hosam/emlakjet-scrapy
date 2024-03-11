import scrapy
import json


class PetlebiSpider(scrapy.Spider):
    name = 'petlebi'
    start_urls = ['https://www.petlebi.com/']
    products_array = []
    products_links = []
    other = []

    def parse(self, response):
        """
        This function parses all the products in the main page.
        """
        products_div = response.css('#products')

        products = products_div.css('.search-product-box')

        for product in products:
            product_link = product.css('.p-link::attr(href)').get()
            self.products_links.append(product_link)
            yield response.follow(
                product_link, callback=self.parse_product_details)

    def parse_product_details(self, response):
        """
        This function parses a product page.
        """
        product_name = response.css('.product-h1::text').get()
        product_price = response.css('.new-price::text').get()
        barkod_div = response.xpath('//div[contains(text(), "BARKOD")]')
        
        # Get the barkod number from barkod_div
        barkod_number = barkod_div.xpath(
            './following-sibling::div/text()').get()
        marka_div = response.xpath('//div[contains(text(), "MARKA")]')
        # Get the marka name from marka_div
        marka_name = marka_div.xpath(
            './following-sibling::div/span/a/text()').get()
        product_description = response.xpath(
            '//span[@id="productDescription"]//text()').getall()
        product_description = ' '.join(
            map(str.strip, product_description)).strip()
        # print("\n\n\nproducts_div", product_name, "\n\n\n\n\n\n")
        product_category = response.xpath(
            '//ol[@class="breadcrumb"]/li[2]//span[@itemprop="name"]/text()').get().strip()

        product_images = response.css('.thumb-link::attr(href)').getall()
        product = {
            'product_URL': response.request.url,
            'product_name': product_name,
            'product_price': product_price,
            'barkod_number': barkod_number,
            'brand_name': marka_name,
            'product_description': product_description,
            'product_category': product_category,
            'product_images': str(product_images),
            'product_stock': '',
            'sku': '',
            'product_id': '',
        }
        # adding the product to products_array
        PetlebiSpider.products_array.append(product)

        yield product

    def closed(self, reason):
        """
        This method is called when the spider is closed.
        Save the products to JSON file here.
        """
        with open("petlebi_products.json", "w", encoding='UTF-8') as file:
            json.dump(PetlebiSpider.products_array, file, ensure_ascii=False)
