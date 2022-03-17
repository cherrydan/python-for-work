import sqlite3 as sq


# уроки по SQLLite (c) selfedu. Бэкап БД при помощи метода iterdump. Запись бэкапа в файл

with sq.connect('cars.db') as conn:
    cur = conn.cursor()

    with open('sql_dump.sql', 'w') as file:
        for sql in conn.iterdump():
            file.write(sql)

