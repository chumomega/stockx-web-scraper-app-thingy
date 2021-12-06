from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class StockxTrendGetter:
    STREETWEAR_URL = 'https://stockx.com/streetwear/most-popular'
    SNEAKER_URL = 'https://stockx.com/sneakers/most-popular'
    PRODUCT_TITLE_ATTRIBUTE = 'css-1x3b5qq'


    def get_top_trending_streetwear(self):
        request = Request(self.STREETWEAR_URL, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(request).read()
        page_soup = BeautifulSoup(source, 'html.parser')
        street_wear_list = page_soup.find_all('div', 'product-tile')
        return list(map(lambda product_div: product_div.find('p', self.PRODUCT_TITLE_ATTRIBUTE).string, street_wear_list))

    def get_top_trending_sneakers(self):
        request = Request(self.SNEAKER_URL, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(request).read()
        page_soup = BeautifulSoup(source, 'html.parser')
        street_wear_list = page_soup.find_all('div', 'product-tile')
        return list(map(lambda product_div: product_div.find('p', self.PRODUCT_TITLE_ATTRIBUTE).string, street_wear_list))
