import sqlite3
from time import sleep
from parser import *

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

for film in data:
    sqlite_insert_query = """INSERT INTO movies_movies
                          (id, title, description, image, is_watched)
                           VALUES
                          (?, ?, ?, ?, ?)""";
    data_tuple = (
        film[2], str(film[0]),
        str(film[1]), str(film[3]),
        str(False), )
    count = cursor.execute(sqlite_insert_query, data_tuple)
    print("Добавлен: ",film[0])
    sleep(0.2)
connection.commit()
connection.close()
