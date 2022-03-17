import sqlite3 as sq

# уроки по SQLLite (c) selfedu.
# команды SELECT. Вывод в печать результата выборки при помощи цикла for

query = """
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5
"""

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute(query)

    for result in cur:
        print(result)

