import scrapy
import time

class TopSpider(scrapy.Spider):
    name = "top"
    start_urls = [
        "https://www.reddit.com/r/hiphopheads/top/?sort=top&t=all"
    ]

    def parse(self, response):
        post_selectors = response.css('div.thing')

        for selector in post_selectors:
            url = selector.css('::attr(data-url)').extract_first()
            domain = selector.css('::attr(data-domain)').extract_first()
            rank = selector.css('::attr(data-rank)').extract_first()
            title = selector.css('a.title::text').extract_first()
            comments_url = selector.css('a.comments::attr(href)').extract_first()
            num_comments = selector.css('a.comments::text').extract_first()
            datetime = selector.css('time::attr(datetime)').extract_first()
            score = selector.css('div.score.unvoted::attr(title)').extract_first()
            yield {
                'url': url,
                'domain': domain,
                'rank': int(rank),
                'title': title,
                'comments_url': comments_url,
                'num_comments': int(num_comments.split()[0]),
                'datetime': datetime,
                'score': int(score)
            }

        time.sleep(0.2)

        next_url = response.css('.next-button a::attr(href)').extract_first()
        yield scrapy.Request(url=next_url, callback=self.parse)