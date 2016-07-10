import urllib.request
from bs4 import BeautifulSoup
import Functions

url = Functions.urlParser()
#url = "https://www.bambino.sk"
domainLanguage = Functions.whereAmI(url)

if domainLanguage[0][1] == "cz":
    add = "/vsechny-produkty?order=price-asc"
    url = url + add

else:
    add = "/vsetky-produkty?order=price-asc"
    url = url + add

soup = Functions.readHTML(url)
domain = domainLanguage[0][0]
if domain == "bigbrands":
    price = Functions.itemPrice("product-box__info__price","span",soup)
    print(price)
elif domain == "prodeti" or domain == "bambino":
    price = Functions.itemPrice("product-box__info--right", "strong",soup)
    print(price)
elif domain == "kolonial":
     price = Functions.itemPrice("product-box__info__price","strong",soup)
     print(price)
else:
    print("Domain is not supported.")