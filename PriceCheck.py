import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.bigbrands.cz/vsechny-produkty?order=price-asc").read()
#print(html)
soup = BeautifulSoup(html)
print(type(soup))
product= soup.find(class_="product-box__info__price")
print(product)
priceTag = product.find("span", {"itemprop" : "price"}).attrs
#dictionary = priceTag.attrs
print(priceTag)
#print(dictionary)
price = float(priceTag['content'])
print(price)
