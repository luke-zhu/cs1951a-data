import scrapy
import datetime
import time

class PostsSpider(scrapy.Spider):
    name = "posts"

    def start_requests(self):
        urls = [
            #'http://web.archive.org/web/*/http://reddit.com/r/hiphopheads',
            'http://web.archive.org/web/20160401000000*/http://reddit.com/r/hiphopheads',
            'http://web.archive.org/web/20150501000000*/http://reddit.com/r/hiphopheads',
            'http://web.archive.org/web/20140715000000*/http://reddit.com/r/hiphopheads',
            'http://web.archive.org/web/20130601000000*/http://reddit.com/r/hiphopheads',
            'http://web.archive.org/web/20120701000000*/http://reddit.com/r/hiphopheads',
            'http://web.archive.org/web/20120701000000*/http://reddit.com/r/hiphopheads',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseArchive)

    def parseArchive(self, response):
        hrefs = response.xpath('//div[@class="day"]/a/@href').extract()

        for href in hrefs:
            url = response.urljoin(href)
            yield scrapy.Request(url=url, callback=self.parseSubreddit)

    def parseSubreddit(self, response):
        date_string = response.url.split('/')[4]
        urls = response.css('a.comments::attr(href)').extract()
        cleaned_urls = ['/'.join(url.split('/')[3:]) for url in urls]

        titles = response.css('a.title::text').extract()
        
        for (title, url) in zip(titles, cleaned_urls):
            yield {
                'title': title,
                'comments_url': url,
                'date': date_string,
            }
        time.sleep(0.5)