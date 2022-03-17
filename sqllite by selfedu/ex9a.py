import sqlite3 as sq

# уроки по SQLLite (c) selfedu. Подключение к БД с обработкой исключений
# метка BEGIN для отката изменений, в случае если что-то пошло не так

conn = None


try:
    conn = sq.connect('cars.db')
    cur = conn.cursor()

    # execute_script = выполнение нескольких SQL-комманд, перечисленных через точку с запятой
    # удаляем все машины, название которых начинается на A
    # и прибавляем к цене всех остальных машин 1000 единиц
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER)
    ;
    BEGIN;
    INSERT INTO cars VALUES(NULL, 'Audi', 52642);
    INSERT INTO cars VALUES(NULL, 'Mercedes', 57127);
    INSERT INTO cars VALUES(NULL, 'Skoda', 9000);
    INSERT INTO cars VALUES(NULL, 'Volvo', 29000);
    INSERT INTO cars VALUES(NULL, 'Bentley', 350000);
    UPDATE cars SET price = price + 10000
    """)
    conn.commit()


except sq.Error as err:
    if conn:
        conn.rollback()
    print('Ошибка выполнения запроса')

finally:
    if conn:
        conn.close()

