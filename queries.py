create_table = '''CREATE TABLE IF NOT EXISTS BikeShare
            (
                TripDuration INT,
                StartTime DATE,
                StopTime DATE,
                StartStationID INT,
                StartStationName TEXT,
                StartStationLatitude FLOAT,
                StartStationLongitude FLOAT,
                EndStationID INT,
                EndStationName TEXT,
                EndStationLatitude FLOAT,
                EndStationLongitude FLOAT,
                BikeID INT,
                UserType TEXT,
                BirthYear INT,
                Gender INT,
                TripDurationinmin INT
            )'''

insert_records = '''INSERT INTO BikeShare (
                            TripDuration,
                            StartTime,
                            StopTime,
                            StartStationID,
                            StartStationName, 
                            StartStationLatitude,
                            StartStationLongitude,
                            EndStationID,
                            EndStationName,
                            EndStationLatitude,
                            EndStationLongitude,
                            BikeID,
                            UserType,
                            BirthYear,
                            Gender,
                            TripDurationinmin
                        ) VALUES(?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''