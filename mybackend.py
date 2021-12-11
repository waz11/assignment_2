import sqlite3
from itertools import chain
from database import Database
import queries

def clean_rows(list):
    res = []
    for r in list:
        res.append(r)
    return res

def get_recommendations(location='', time=0, amount=5):
    query = "SELECT StartStationName FROM BikeShare LIMIT 5;"
    res = Database().select_query(query)
    res = list(chain.from_iterable(res))
    recommendations = []
    for r in res:
        recommendations.append(r)
    print("recommendations: ",recommendations)
    return recommendations

def is_location_exists(location):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = "select StartStationName from BikeShare where StartStationName LIKE '%"+location+"%' limit 1;"
    res = cursor.execute(query).fetchall()
    return len(res)>0


if __name__ == '__main__':
    db = Database()
    db.test()

