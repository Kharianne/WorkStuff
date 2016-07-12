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
        print("URL argument missing")
        exit()
    else:
        return url
def urlParserVouchers():
    parser = argparse.ArgumentParser(description="Fill in attributes for vouchers")
    parser.add_argument('--url', action = "store", type = str)
    parser.add_argument('--proc', action="store", type=float, default=33)
    parser.add_argument('--fix', action="store", type=float, default=150)
    parser.add_argument('--kred', action="store", type=float, default=99)
    parser.add_argument('--brand', action="store", type=str, default=False)
    parser.add_argument('--cat', action="store", type=str, default=False)
    args = parser.parse_args()
    values = vars(args)
    return values

#Parse url into domain and cz/sk
def whereAmI(url):
    try:
        domainLanguage = re.findall('^https?://(?:www)\.(.+)\.(.+)', url)
        return domainLanguage
    except:
        print("URL neni v pozadovanem formatu!")
        exit()

#Returns BS4 object to work with
def readHTML(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

#Finds first product on a page and returns its price
#class_ - refers to class of div with price
#tag - refers to tag with price inside div above
#soup - refers to BS4 object
def itemPrice(class_, tag, soup):
    product= soup.find(class_=class_)
    priceTag = product.find(tag, {"itemprop": "price"}).attrs
    price = float(priceTag['content'])
    return price
