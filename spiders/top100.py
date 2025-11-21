import scrapy
from scrapy_playwright.page import PageMethod
# Cut CUt Cut

class AmazonBestSellerSpider(scrapy.Spider):
    name = "amazon_bs"
    allowed_domains = ["amazon.ae"]
    urls_list = [
        "https://www.amazon.ae/gp/bestsellers/pet-products/15198290031",                                            #Food
        "https://www.amazon.ae/gp/bestsellers/pet-products/15198290031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Food
        "https://www.amazon.ae/gp/bestsellers/pet-products/17453403031",                                            #Dehydrated
        "https://www.amazon.ae/gp/bestsellers/pet-products/17453403031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Dehydrated   
        "https://www.amazon.ae/gp/bestsellers/pet-products/15240108031",                                            #Dry
        "https://www.amazon.ae/gp/bestsellers/pet-products/15240108031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Dry
        "https://www.amazon.ae/gp/bestsellers/pet-products/15240109031",                                            #Food
        "https://www.amazon.ae/gp/bestsellers/pet-products/15240109031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Food Toppers
        "https://www.amazon.ae/gp/bestsellers/pet-products/17453404031",                                            #Freeze
        "https://www.amazon.ae/gp/bestsellers/pet-products/17453404031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Freeze-Dried
        "https://www.amazon.ae/gp/bestsellers/pet-products/85444049031",                                            #Diet
        "https://www.amazon.ae/gp/bestsellers/pet-products/85444049031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Diet
        "https://www.amazon.ae/gp/bestsellers/pet-products/85169053031",                                            #Canned
        "https://www.amazon.ae/gp/bestsellers/pet-products/85169053031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2",   #Canned
        "https://www.amazon.ae/gp/bestsellers/pet-products/85169052031"                                             #Pouches
        "https://www.amazon.ae/gp/bestsellers/pet-products/85169052031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"    #Pouches
    ]

    def start_requests(self):
        for url in self.urls_list:
            yield scrapy.Request(
                url,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [PageMethod("wait_for_selector", "body"),
                                                PageMethod("wait_for_timeout", 2000),
                                                PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                                                PageMethod("wait_for_timeout", 1000),
                                                PageMethod("evaluate", "window.scrollBy(0, -window.innerHeight)"),
                                                PageMethod("wait_for_timeout", 1000),
                                                PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                                                PageMethod("wait_for_timeout", 2000),
                                                PageMethod("evaluate", "window.scrollBy(0, -window.innerHeight)"),
                                                PageMethod("wait_for_timeout", 2000),
                                                PageMethod("evaluate", "window.scrollBy(0, -window.innerHeight)"),
                                                PageMethod("wait_for_timeout", 2000)]
                },
            )

    async def parse(self, response):
        links = response.url
        if links == ("https://www.amazon.ae/gp/bestsellers/pet-products/15198290031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/15198290031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Food"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/17453403031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/17453403031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Dehydrated"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/15240108031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/15240108031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"): 
            fields = "Dry"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/15240109031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/15240109031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Food Toppers"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/17453404031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/17453404031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Freeze-Dried"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/85444049031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/85444049031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Diet"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/85169053031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/85169053031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Canned"
        elif links == ("https://www.amazon.ae/gp/bestsellers/pet-products/85169052031") or (links == "https://www.amazon.ae/gp/bestsellers/pet-products/85169052031/ref=zg_bs_pg_2_pet-products?ie=UTF8&pg=2"):
            fields = "Pouches"
        else:
            fields = "N/A"
            pass
        ranks = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/div[1]/div[1]/span/text()").getall()
        asins = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/@data-asin").getall()
        titles = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/div[2]/span/div/div/div/a/span/div/text()").getall()
        stars = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/div[2]/span/div/div/div/div[1]/div/a/i/span/text()").getall()
        people = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/div[2]/span/div/div/div/div[1]/div/a/span/text()").getall()
        # prices = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/div[2]/span/div/div/div/div[2]/div/div/a/div/span/span/text()").getall()
        try:
            prices = response.xpath("//li[contains(@class,'zg-no-numbers')]/span/div/div/div/div[2]/span/div/div/div/div[2]/div/div/a/div/span/span/text()").getall()
            if not prices:
                prices = "NA"
        except:
            pass

        for rank, asin, title, star, public, price in zip(ranks, asins, titles, stars, people, prices):
            yield {
                "field": fields,
                "rank": rank.replace("#", ""),
                "asin": asin,
                "title": title,
                "star": star.replace(' out of 5 stars',''),
                "public": public,
                "price": price.replace('AED', '').replace('Â', '').strip() if price else "NA"
                }