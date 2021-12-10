import sqlite3
from itertools import chain
from database import Database


def get_recommendations(location='', time=0, amount=5):
    connection = sqlite3.connect('database.db')
    query = "SELECT StartStationName FROM BikeShare LIMIT 5;"
    res = Database().select_query(query)
    res = list(chain.from_iterable(res))
    recommendations = []
    for r in res:
        recommendations.append(r)
    print("recommendations: ",recommendations)
    return recommendations


if __name__ == '__main__':
    db = Database()
    db.test()
