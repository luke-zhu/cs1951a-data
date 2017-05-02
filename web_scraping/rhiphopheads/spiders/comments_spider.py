import scrapy
import time
import random

from textblob import TextBlob

class CommentsSpider(scrapy.Spider):
    name = "comments"
    start_urls = [
        "https://www.reddit.com/r/hiphopheads/top/?sort=top&t=all"
    ]

    def parse(self, response):
        time.sleep(random.random())
        post_selectors = response.css('div.thing')

        for selector in post_selectors:
            comments_url = selector.css('a.comments::attr(href)').extract_first()
            yield scrapy.Request(url=comments_url, callback=self.parseComments)

        next_url = response.css('.next-button a::attr(href)').extract_first()
        yield scrapy.Request(url=next_url, callback=self.parse)

    def parseComments(self, response):
        time.sleep(random.random())
        comments = ' '.join(response.css('div.sitetable div.md p::text').extract())
        blob = TextBlob(comments)
        yield {
            'url': response.url,
            'polarity': blob.sentiment.polarity,
            'subjectivity': blob.sentiment.subjectivity,
        }