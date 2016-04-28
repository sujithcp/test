import re

import feedparser
import urllib
from bs4 import *

from generals import *
from lxml import html

class Site:
    def __init__(self,url,type,extract):
        self.url = url
        self.type=type
        self.extract = extract


def fetch(site):
    fp = feedparser.parse(site.url)
    for i in range(0, len(fp['entries']) - 1):
        print(fp['entries'][i]['title'], fp['entries'][i]['link'])
        text = get_paragraph(get_text_from_url(fp['entries'][i]['link']), site)
        text = re.sub('<.*?>', '\n', text)
        title = str(i)+fp['entries'][i]['title'].split()[0]+'.txt'
        createFile('fetched_data/'+site.type+'/',title, text)



def get_text_from_url(url):
    with urllib.request.urlopen(url) as response:
        html_doc = response.read()
    return html_doc

def get_paragraph(html,site):
    text = html
    for i in site.extract:
        p = BeautifulSoup(text, 'html.parser')
        tmp =  p.find_all(i[0], attrs=i[1])
        text = ""
        for j in tmp:
            text+=str(j)
    return text








'''
    fp = feedparser.parse('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml')

for i in range (0,len(fp['entries'])-1):
    print(fp['entries'][i]['title'],fp['entries'][i]['link'])
    print(get_paragraph(get_text_from_url(fp['entries'][i]['link'])))
    text = get_paragraph(get_text_from_url(fp['entries'][i]['link']))
    createFile('./', str(i)+'.txt', text)

    '''




site1 = Site('http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml', 'entertainment', [['div', {"class": "story-body__inner"}], ['p',None]])

fetch(site1)
