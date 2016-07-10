import urllib.request
import Functions
import bs4

url = Functions.urlParser()
html = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(html)
campaignUrls = []
for campaign in soup.find_all('div',class_='grid__cell'):
    tags = campaign.find_all('a')
    titles = campaign.find_all('img')
    for tag in tags:
        urlCampaign = tag.get('href', None)
        if urlCampaign.startswith('/kampane') and urlCampaign not in campaignUrls:
            campaignUrls.append(urlCampaign)
    if len(campaignUrls) == 0:
        print("WARNING! There is no campaign!")
for campaignUrl in campaignUrls:
    goToCampaign = url + campaignUrl
    print(goToCampaign)
    html = urllib.request.urlopen(goToCampaign).read()
    soup = bs4.BeautifulSoup(html)
    for filter in soup.find_all('div',class_='filter__tags'):
        elem = filter.find('strong')
        if elem is None: continue
        products = elem.get_text('strong')
        numberOfproducts = int(products)
        if numberOfproducts < 5:
            print ("WARNING! There are less than 5 ks in " + goToCampaign + " campaign!")
        else:
            print(numberOfproducts)
        break
    else:
        print("WARNING! Campaign has no products!")

