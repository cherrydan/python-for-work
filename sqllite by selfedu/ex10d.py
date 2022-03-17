import sqlite3 as sq


# уроки по SQLLite (c) selfedu. Создание БД непосредственно в памяти
data = [
    ('car', 'машина'),
    ('leather', 'кожа'),
    ('house', 'дом'),
    ('tree', 'дерево'),
    ('color', 'цвет')
]

# ключевое = параметр :memory: помещает БД в память
with sq.connect(':memory:') as conn:
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS dict (
    eng TEXT,
    rus TEXT)
    """)

    cur.executemany("""
    INSERT INTO dict VALUES (?, ?)
    """, data)

    cur.execute("""
    SELECT rus FROM dict WHERE eng LIKE 'c%'
    """)

    print(cur.fetchall())
