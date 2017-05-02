import requests
from scrapy.selector import Selector

def getComments(url):
    r = requests.get(url)
    comments = Selector(text=r.text).xpath('///div[@class="md"]/p/text()').extract()[3:]

    return comments

if __name__ == '__main__':
    print(getComments('https://www.reddit.com/r/hiphopheads/comments/5z6evc/playboi_carti_set_to_release_his_debut_mixtape/'))

