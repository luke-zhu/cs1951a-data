import scrapy
import time
import random

class BillboardSpider(scrapy.Spider):
    name = "billboard"
    start_urls = [
        "http://www.billboard.com/charts/r-b-hip-hop-albums"
    ]

    def parse(self, response):
        week = response.css('time::attr(datetime)').extract_first()
        song_selectors = response.css('article.chart-row')

        for selector in song_selectors:
            rank = selector.css('span.chart-row__current-week::text').extract_first()
            title = selector.css('.chart-row__song::text').extract_first()
            artist = ' '.join(selector.css('.chart-row__artist::text').extract_first().split())
            yield {
                'rank': int(rank),
                'title': title,
                'artist': artist,
                'week': week,
            }

        time.sleep(random.random())
        
        next_url = response.css('#chart-nav > a::attr(href)').extract_first()
        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)