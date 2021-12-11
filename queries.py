create_table = '''CREATE TABLE IF NOT EXISTS BikeShare
            (
                TripDuration INT,
                StartStationName TEXT,
                EndStationName TEXT,
                TripDurationinmin INT
            )'''


insert_records = '''INSERT INTO BikeShare (
                            TripDuration,
                            StartStationName,
                            EndStationName,
                            TripDurationinmin
                        ) VALUES(?,?,?,?)'''

get_locations = '''SELECT DISTINCT StartStationName FROM BikeShare ORDER BY StartStationName ASC'''