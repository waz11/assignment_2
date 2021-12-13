import sqlite3
from itertools import chain
from database_func import Database
import queries

def clean_rows(list):
    res = []
    for r in list:
        print(r)
        res.append(r.translate("(',)"))
    return res


def is_legal_input(location='', time='', amount=''):
    errors = []
    return errors


def get_recommendations(location='', time=0, amount=5):
    errors = is_legal_input(location, time, amount)
    if len(errors) is not 0:
        return errors
    # query = "SELECT StartStationName FROM BikeShare LIMIT 5;"
    # res = Database().select_query(query)
    # res = list(chain.from_iterable(res))
    # recommendations = clean_rows(res)

    recommendations = [location, time, amount]

    print("recommendations: ",recommendations)
    return recommendations

def is_location_exists(location):
    query = "select StartStationName from BikeShare where StartStationName LIKE '%"+location+"%' limit 1;"
    res = Database().select_query(query)
    return len(res)>0

def number_of_locations():
    query = "select COUNT(DISTINCT StartStationName) from BikeShare;"
    res = Database().select_query(query)
    return res[0][0]


if __name__ == '__main__':
    db = Database()
    db.test()
