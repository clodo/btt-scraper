import scraperwiki
import lxml.html

ROOT = 'http://www.btt.com.ar/'
URL_BASE = ROOT + 'bicicleteria/Buenos-Aires.shtml'

def parseBikeShop(bike_shop_url):
    html = scraperwiki.scrape(ROOT + bike_shop_url)
    searchTree = lxml_html.fromstring(html)

    data = dict()

    field_name = searchTree.xpath('//h2/text()')[0].encode('utf-8','ignore').strip(' \t\n\r')
    data['name'] = field_name

    scraperwiki.sqlite.save(unique_keys=['name'], data=data)

def runScraper(provincia):
    html = scraperwiki.scrape(URL_BASE + ".shtml")
    searchTree = lxml_html.fromstring(html)

    for link in searchTree.cssselect('tr a[href^="/bici/"]'):
        parseBikeShop(link.attrib['href'])

runScraper("Buenos-Aires")
