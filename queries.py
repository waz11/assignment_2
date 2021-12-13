
# query for create the main table of database
create_table = '''CREATE TABLE IF NOT EXISTS BikeShare
            (
                TripDuration INT,
                StartStationName TEXT,
                EndStationName TEXT,
                TripDurationinmin INT
            )'''

# query for inserting rows from csv file to the databse
insert_records = '''INSERT INTO BikeShare (
                            TripDuration,
                            StartStationName,
                            EndStationName,
                            TripDurationinmin
                        ) VALUES(?,?,?,?)'''

# query for getting the start station names from the database
get_locations = '''SELECT DISTINCT StartStationName FROM BikeShare ORDER BY StartStationName ASC'''