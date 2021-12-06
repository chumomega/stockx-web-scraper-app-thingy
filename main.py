# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os
import time
from StockxTrendGetter import StockxTrendGetter


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    top_trend_getter = StockxTrendGetter()

    begin = time.perf_counter()
    top_sneakers = top_trend_getter.get_top_trending_sneakers()
    top_streetwear = top_trend_getter.get_top_trending_streetwear()
    end = time.perf_counter()

    print("all the sneakers: ", top_sneakers)
    print("all the streetwear: ", top_streetwear)
    print("time_to_run: ", (end - begin))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
