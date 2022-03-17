import sqlite3 as sq

# уроки по SQLLite (c) selfedu. Методы API: Fetchall, fetchmany, fetchone, Binary, iterdump

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

with sq.connect('cars.db') as conn:

    cur = conn.cursor()
    # преобразуем наши выходные данные в словарь
    cur.row_factory = sq.Row

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER)
    """)

    # cur.executemany(""" INSERT INTO cars  VALUES(NULL, ?, ?) """, cars)

    cur.execute(""" SELECT model, price from cars""")

    # cur после выборки является итерируемым объектом, и его можно перебрать в цикле

    for row in cur:
        print(row['model'], row['price'])

