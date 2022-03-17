import sqlite3 as sq

# уроки по SQLLite (c) selfedu.
# создание таблицы users через python

query = """
CREATE TABLE IF NOT EXISTS users (
name TEXT NOT NULL,
sex INTEGER NOT NULL DEFAULT 1,
old INTEGER,
score INTEGER)
"""

query2 = """ DROP TABLE IF EXISTS users """

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute(query)
