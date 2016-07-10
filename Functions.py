import argparse
import re
import urllib.request
from bs4 import BeautifulSoup



#Reads url from command line
def urlParser():
    parser = argparse.ArgumentParser(description="Fill in url")
    parser.add_argument('--url', action = "store", type = str)
    args = parser.parse_args()
    values = vars(args)
    url = (values['url'])
    if url is None:
        print ("URL argument missing")
        exit()
    else:
        return url

#Parse url into domain and cz/sk
def whereAmI(url):
    try:
        domainLanguage = re.findall('^https?://(?:www)\.(.+)\.(.+)', url)
        return domainLanguage
    except:
        print ("URL neni v pozadovanem formatu!")
        exit()

#Returns BS4 object to work with
def readHTML(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

#Finds first product on a page and returns its price
def itemPrice(class_, tag, soup):
    product= soup.find(class_=class_)
    priceTag = product.find(tag, {"itemprop" : "price"}).attrs
    price = float(priceTag['content'])
    return price
