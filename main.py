# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    if 'soup_source' in os.environ:
        source = os.environ['soup_source']
    else:
        begin = time.perf_counter()
        request = Request('https://stockx.com/streetwear/most-popular', headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(request).read()
        # os.environ['soup_source'] = source
        end = time.perf_counter()
        print("time_to_run: ", (end-begin))

    page_soup = BeautifulSoup(source, 'html.parser')

    street_wear_list = page_soup.find_all('div', 'product-tile')
    top_products = list(map(lambda product_div: product_div.find('p', 'css-1x3b5qq').string, street_wear_list))

    print("This is the page title: ", page_soup.title.string)
    print("all the streetwear: ", top_products)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
