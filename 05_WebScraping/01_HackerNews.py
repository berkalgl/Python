import requests
from bs4 import BeautifulSoup
import pprint

# Bs4 actually allows us to use the HTML and grap different DATA
# so it allows us to use that data that we have gathered to do whatever
# we want to it to scrape it.

# requests allows us to download the html

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

# gets the only body tag
# print(soup.body)
# finds the all divs
# print(soup.find_all('div'))
# finds the first thing
# print(soup.find('a'))
# finds with the id
# print(soup.find(id='score_20514755'))
# finds with css class selector
# print(soup.select('.score'))

links = soup.select('.titlelink')
subtexts = soup.select('.subtext')

def sort_stories_by_votes(hnlist, sort_key):
    return sorted(hnlist, key= lambda k:k[sort_key], reverse=True)

def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtexts[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().split(' ')[0])
            if points > 99:
                hn.append({'title': title, 'link' : href, 'votes':points})
    return sort_stories_by_votes(hn, 'votes')

pprint.pprint(create_custom_hn(links, subtexts))