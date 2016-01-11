import scraperwiki
from lxml import html as lxml_html
import urlparse
import re

ROOT_URL = 'http://www.btt.com.ar/'

def parseBikeShop(bike_shop_url):
    html = scraperwiki.scrape(ROOT_URL + bike_shop_url)
    searchTree = lxml_html.fromstring(html)

    data = dict()

    field_name = searchTree.xpath('//h2/text()')[0]
    data['name'] = field_name

    field_address = searchTree.xpath('//address/text()')[3]
    data['address'] = field_address

    field_website = searchTree.xpath('//address/dt/a/text()')
    if field_website:
        data['website'] = field_website[0]
    else:
        data['website'] = "-"


    '''
    .re(r'Sitio web:\s*(.*)')

    field_latitude = searchTree.xpath('//address/dt/a/text()')[0].encode('utf-8','ignore').strip(' \t\n\r')
    data['latitude'] = field_latitude

    field_longitude = searchTree.xpath('//address/dt/a/text()')[0].encode('utf-8','ignore').strip(' \t\n\r')
    data['latitude'] = field_longitude

    sel.xpath('//a[contains(@href, "image")]/text()').re(r'Name:\s*(.*)')
    '''

    print data

    scraperwiki.sqlite.save(unique_keys=['name'], data=data)

def runScraper(provincia):
    print 'Scraping bike shops of ' + provincia
    html = scraperwiki.scrape(ROOT_URL + 'bicicleteria/' + ".shtml")
    searchTree = lxml_html.fromstring(html)

    for link in searchTree.cssselect('tr a[href^="/bici/"]'):
        print link.attrib['href']
        parseBikeShop(link.attrib['href'])

runScraper("Buenos-Aires")
