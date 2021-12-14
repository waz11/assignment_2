from database_func import Database

# the function return values from database query with no symbols
def clean_rows(list):
    res = []
    for r in list:
        print(r)
        res.append(r.translate("(',)"))
    return res

isInt = lambda a : a.isdigit() and int(a) > 0

#the function returns a list of errors if the inputs aren't as expected
def is_legal_input(location='', time='', amount=''):
    errors = []
    if not is_location_exists(location):
        errors.append('* The start location is not exists')
    if not isInt(time):
        errors.append('* time is not a number bigger than 0')
    if not isInt(amount):
        errors.append('* num of recommendations is not a number bigger than 0')
    return errors

# the function gets location, time and number of time for traveling
# and return recommendations of the end place of optional trips
def get_recommendations(location='', time=0, amount=5):
    errors = is_legal_input(location, time, amount)
    if len(errors) is not 0:
        return errors
    # query = "SELECT StartStationName FROM BikeShare LIMIT 5;"
    # res = Database().select_query(query)
    # res = list(chain.from_iterable(res))
    # recommendations = clean_rows(res)

    recommendations = [location, time, amount]
    return recommendations

# the function returns true if the location is exists in the database
def is_location_exists(location):
    query = "select StartStationName from BikeShare where StartStationName = '"+location+"' COLLATE NOCASE limit 1;"
    res = Database().select_query(query)
    return len(res)>0

# the function returns thr enumber of locations exist in tha data
def number_of_locations():
    query = "select COUNT(DISTINCT StartStationName) from BikeShare;"
    res = Database().select_query(query)
    return res[0][0]


if __name__ == '__main__':
    db = Database()
    db.test()