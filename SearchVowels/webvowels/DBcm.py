import mysql.connector

"""

Создание менеджера контекста
нам понадобится переопределить три метода

"""


class UseDatabase:
    # метод __init__ должен принять словарь с параметрами базы данных
    def __init__(self, config: dict):
        self.configuration = config

    # метод __enter__ делает всю полезную работу с базой
    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    # метод __exit__ закрывает соединение с базой
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
