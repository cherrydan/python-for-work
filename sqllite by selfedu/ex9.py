import sqlite3 as sq

# уроки по SQLLite (c) selfedu. Создание таблицы и заполнение данными по шаблону.
# (я тут кое-что улучшил (danny)

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

table_name = 'cars'
update_field_name = 'price'

create_table = """
CREATE TABLE IF NOT EXISTS {} (
car_id INTEGER PRIMARY KEY AUTOINCREMENT, 
model TEXT,
price INTEGER)
""".format(table_name)

insert_data = """
INSERT INTO {} VALUES (NULL, ?, ?)
""".format(table_name)

update_data = """
UPDATE {} SET {} = :Price WHERE model LIKE 'A%'
""".format(table_name, update_field_name)

delete_a_name = """
DELETE FROM {} WHERE model LIKE 'A%'
""".format(table_name)

update_price = """
UPDATE {} SET {} = {} + 1000
""".format(table_name, update_field_name, update_field_name)

with sq.connect('cars.db') as conn:
    cur = conn.cursor()

    cur.execute(create_table)

    # перебираем вручную циклом for
    for car in cars:
        cur.execute(insert_data, car)

    # используем автоматический перебор, при помощи executemany
    cur.executemany(insert_data, cars)

    # использование именованых параметров в запросе. Цену всех автомобилей, название которых
    # начинается на букву А устанавливаем в 0, значение будет браться по ключу Price из словаря
    cur.execute(update_data, {'Price': 0})

    # execute_script = выполнение нескольких SQL-комманд, перечисленных через точку с запятой
    # удаляем все машины, название которых начинается на A
    # и прибавляем к цене всех остальных машин 1000 единиц
    cur.executescript(delete_a_name +
                      ' ; ' + update_price)

