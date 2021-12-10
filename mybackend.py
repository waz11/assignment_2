from itertools import chain
from database import Database
import queries


def ron():
    res = Database().select_query(queries.get_locations)
    res = list(chain.from_iterable(res))
    ans = []
    for r in res:
        ans.append(r)
    print(ans)
    print('bayside park' in res)
    return ans


def get_recommendations(location='', time=0, amount=5):
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
    # db.test()
    ron()
