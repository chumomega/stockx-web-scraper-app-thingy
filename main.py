# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import random
from StockxTrendGetter import StockxTrendGetter
from cassandra.cluster import Cluster


# Press the green button in the gutter to run the script.
def getMostPopularBrand(products: list):
    brands = list(map(lambda product: product.split()[0], products))
    # sub_brands = filter(lambda product: product.split()[1], products)

    brand_counter = getItemCounter(brands)
    # sub_brand_counter = getItemCounter(sub_brands)

    return getMostPopularItem(brand_counter)
    # top_sub_brand = getMostPopularItem(sub_brand_counter)
    # return top_brand


# Expecting a dictionary with key = str, value = count
def getMostPopularItem(item_counter: dict) -> str:
    return max(item_counter, key=item_counter.get)


def getItemCounter(items: list) -> dict:
    item_counter = {}

    for item in items:
        if item in item_counter:
            item_counter[item] += 1
        else:
            item_counter[item] = 1

    return item_counter


if __name__ == '__main__':
    cluster = Cluster()
    session = cluster.connect('main_db')

    top_trend_getter = StockxTrendGetter()

    begin = time.perf_counter()
    top_sneakers = list(map(
        lambda row: row.product,
        session.execute('SELECT date, type, product, id from top_products').all()
    ))
    num_top_sneakers = len(top_sneakers)
    if num_top_sneakers == 0:
        print("Scraping web for data")
        top_sneakers = top_trend_getter.get_top_trending_sneakers()
        for sneaker in top_sneakers:
            session.execute(
                """
                INSERT INTO top_products (date, type, product, id)
                VALUES (%s, %s, %s, %s)
                """,
                (datetime.datetime.now().strftime('%x'), 'sneaker', str(sneaker), random.randint(0, 100000))
            )
    else:
        print("Successfully got data from Cassandra")

    end = time.perf_counter()
    print("time_to_run sneaker retrieval: ", (end - begin))

    top_streetwear = top_trend_getter.get_top_trending_streetwear()

    top_brand = getMostPopularBrand(top_sneakers)

    print("Top Brand: ", top_brand)
    cluster.shutdown()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
