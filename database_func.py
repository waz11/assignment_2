import csv
import sqlite3
import queries as query


class Database:
    def __init__(self):
        self.build()


    def select_query(self, query):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        res = cursor.execute(query).fetchall()
        connection.commit()
        connection.close()
        return res

    def build(self, path='BikeShare.csv'):
        # https://www.geeksforgeeks.org/how-to-import-a-csv-file-into-a-sqlite-database-table-using-python/
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(query.create_table)

        table_size = self.select_query("select count(*) from BikeShare")[0][0]
        if table_size is 0:
            file = open(path)
            reader = csv.reader(file)
            next(reader)
            included_cols = [0, 4, 8, 15]
            for row in reader:
                content = list(row[i] for i in included_cols)
                cursor.execute(query.insert_records, content)
            connection.commit()
            connection.close()
        return connection

    def test(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        select_all = "SELECT * FROM BikeShare LIMIT 5;"
        rows = cursor.execute(select_all).fetchall()
        for r in rows:
            print(r)
        connection.commit()
        connection.close()


if __name__ == '__main__':
    db = Database()
    db.test()
