import sqlite3 as sq

# уроки по SQLLite (c) selfedu.
# команды SELECT. Вывод в печать одного результата (fetchone) и нескольких (fetchmany)

query = """
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5
"""

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute(query)

    result1 = cur.fetchone()

    result_m = cur.fetchmany(2)

    print(result1)
    print(result_m)
