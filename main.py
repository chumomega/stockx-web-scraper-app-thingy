# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
import datetime
import random
from StockxTrendGetter import StockxTrendGetter
from cassandra.cluster import Cluster


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cluster = Cluster()
    session = cluster.connect('main_db')
    # session.set_keyspace('top_products')

    top_trend_getter = StockxTrendGetter()

    begin = time.perf_counter()
    # session.execute('USE top_products')
    # print("Date: ", )
    top_sneakers = session.execute('SELECT date, type, product, id from top_products').all()
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
                (datetime.datetime.now().strftime('%x'), 'sneaker', str(sneaker), random.randint(0,100000))
            )
    else:
        print("Successfully got data from Cassandra")

    end = time.perf_counter()
    print("time_to_run sneaker retrieval: ", (end - begin))

    top_streetwear = top_trend_getter.get_top_trending_streetwear()

    print("1st sneaker: ", top_sneakers[0])
    print("2nd sneaker: ", top_sneakers[1])
    print("num sneakers in db: ", num_top_sneakers)
    # print("all the streetwear: ", top_streetwear)
    cluster.shutdown()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
