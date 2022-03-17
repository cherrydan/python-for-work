import sqlite3 as sq


# уроки по SQLLite (c) selfedu. Бэкап БД при помощи метода iterdump. Восстановление базы из дампа

with sq.connect('cars_backup.db') as conn:
    cur = conn.cursor()

    with open('sql_dump.sql', 'r') as file:
        sql = file.read()

        cur.executescript(sql)