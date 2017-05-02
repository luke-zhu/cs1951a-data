import scrapy
import time
import random

class GeniusSpider(scrapy.Spider):
    name = "genius"
    start_urls = [
        "https://genius.com/groups/rap-genius/discussions/pagination?page=5987"
    ]

    def parse(self, response):
        post_selectors = response.css('div.discussion_summary')

        for selector in post_selectors:
            url = selector.css('a.discussion_summary_title::attr(href)').extract_first()
            title = selector.css('h1.subject::text').extract_first().strip()
            num_comments = selector.css('span.post_count::text').extract_first()
            score = selector.css('span.votes_total::text').extract_first()
            excerpt = selector.css('p.excerpt::text').extract_first().strip()
            datetime = ''.join(selector.css('span::attr(data-timeago)').extract())
            yield {
                'url': url,
                'title': title,
                'num_comments': int(num_comments.split()[0]),
                'datetime': datetime,
                'score': int(score),
                'excerpt': excerpt,
            }

        # time.sleep(random.random() / 10)

        next_url = response.css('a.next_page::attr(href)').extract_first()
        yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)