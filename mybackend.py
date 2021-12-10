import csv
import sqlite3
from itertools import chain

import queries as query


def get_recommendations(location='', time=0, amount=5):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    query = "SELECT StartStationName FROM BikeShare LIMIT 5;"
    res = cursor.execute(query).fetchall()
    res = list(chain.from_iterable(res))
    recommendations = []
    for r in res:
        recommendations.append(r)

    print("recommendations: ",recommendations)

    connection.commit()
    connection.close()
    return recommendations


def db_build():
    # https://www.geeksforgeeks.org/how-to-import-a-csv-file-into-a-sqlite-database-table-using-python/
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query.create_table)

    file = open('BikeShare.csv')
    contents = csv.reader(file)
    next(contents)
    cursor.executemany(query.insert_records, contents)

    select_all = "SELECT * FROM BikeShare LIMIT 5;"
    rows = cursor.execute(select_all).fetchall()
    # for r in rows:
    #     print(r)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    db_build()
    get_recommendations()