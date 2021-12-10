import csv
import sqlite3
import queries as query


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
    for r in rows:
        print(r)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    db_build()