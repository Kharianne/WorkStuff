import urllib.request
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://www.bigbrands.cz/vsechny-produkty?order=price-asc").read()
soup = BeautifulSoup(html)
product= soup.find(class_="product-box__info__price")
priceTag = product.find("span", {"itemprop" : "price"}).attrs
price = float(priceTag['content'])
if price < 1:
	print('There is some product below 1 CZK')
print(price)
