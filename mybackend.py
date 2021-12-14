from database_func import Database

# the function return values from database query with no symbols
def clean_rows(list):
    res = []
    for r in list:
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

def find_max_time(listT):
    max_time = 0
    for l in listT:
        tmp = list(l)
        if len(tmp) > 1:
            temp_time = tmp[1]
            max_time = max(max_time, temp_time)
    # print(max_time)
    return max_time

def replace_empty_time_with_max_time(listT, max_time):
    new_list_location_time = []
    for l in listT:
        tmp = list(l)
        if len(tmp) == 1:
            new_tuple = (tmp[0],max_time )
            new_list_location_time.append(new_tuple)
        else:
            new_list_location_time.append(l)
    # print(new_list_location_time)
    return new_list_location_time


def get_sorted_recommendations(station_and_time=[], time=0):
    final_list_recommendations = []
    for t in station_and_time:
        tmp = list(t)
        tmp[1] = abs(time - tmp[1])
        tmp = tuple(tmp)
        final_list_recommendations.append(tmp)
        # print(final_list_recommendations)
    final_list_recommendations = sorted(final_list_recommendations, key=lambda tup: (tup[1], tup[0]))
    # print(final_list_recommendations)
    return final_list_recommendations


# the function gets location, time and number of time for traveling
# and return recommendations of the end place of optional trips
def get_recommendations(location='', time=0, amount=5):
    errors = is_legal_input(location, time, amount)
    if len(errors) > 0:
        return errors
    # query = "SELECT StartStationName FROM BikeShare LIMIT 5;"
    # res = Database().select_query(query)
    # res = list(chain.from_iterable(res))
    # recommendations = clean_rows(res)
    time = int(time)
    amount = int(amount)
    query = "SELECT EndStationName, TripDurationinmin FROM BikeShare WHERE StartStationName = '"+location+"' COLLATE NOCASE;"
    res = Database().select_query(query)
    res = set(res)
    res = list(res)
    location_time_list = replace_empty_time_with_max_time(res, find_max_time(res))
    recommendations = get_sorted_recommendations(location_time_list, time)
    recommendations = remove_duplicate_locations(recommendations)
    rec = [i[0] for i in recommendations[:amount]]
    return rec

def remove_duplicate_locations(recommendations_list):
    clean_recommendations_list = [recommendations_list[0]]
    recommendations_list.remove(recommendations_list[0])
    for i in recommendations_list:
        location, times = zip(*clean_recommendations_list)
        if i[0] not in location:
            clean_recommendations_list.append(i)
    # print(clean_recommendations_list)
    return clean_recommendations_list

def print_list(list):
    for row in list:
        print(row)

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
    # db = Database()
    # db.test()
    rec = get_recommendations('Oakland Ave','1','10000000000')
    print_list(rec)