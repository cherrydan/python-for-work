import sqlite3 as sq


# уроки по SQLLite (c) selfedu. Методы API: Fetchall, fetchmany, fetchone, Binary, iterdump

def readAva(n):
    try:
        with open(f"avas/{n}.png", 'rb') as file:
            return file.read()
    except IOError as err:
        print(err)
        return False


def writeAva(name, data):
    try:
        with open(name, 'wb') as file:
            file.write(data)
    except IOError as err:
        print(err)
        return False


with sq.connect('cars.db') as conn:
    conn.row_factory = sq.Row
    cur = conn.cursor()

    # тип данных BLOB - бинарные данные
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    ava BLOB,
    score INTEGER)
    """)

    # читаем аву
    img = readAva(1)

    if img:
        binary = sq.Binary(img)  # преобразуем в бинарные данные
        cur.execute("""
        INSERT INTO users VALUES('Шикса1', ?, 10000)
        """, (binary,))

    img2 = readAva(2)

    if img2:
        binary = sq.Binary(img2)
        cur.execute("""
        INSERT INTO users VALUES('Кот', ?, 100000)
        """, (binary,))

    img3 = readAva(3)

    if img3:
        binary = sq.Binary(img3)
        cur.execute("""
        INSERT INTO users VALUES('Шикса2', ?, 50000)
        """, (binary,))

    cur.execute("""
    SELECT ava FROM users LIMIT 1 
    """)

    img = cur.fetchone()['ava']

    writeAva('out.jpg', img)
