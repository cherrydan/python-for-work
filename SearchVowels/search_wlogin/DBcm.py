import mysql.connector

"""

Создание менеджера контекста
нам понадобится переопределить три метода

"""


# TODO создаём пустые классы-исключения для обработки проблем с нашим менеджером контеста
class ConnectionErr(Exception):
    pass


class CredentialsErr(Exception):
    pass


class UseDatabase:
    # метод __init__ должен принять словарь с параметрами базы данных
    def __init__(self, config: dict):
        self.configuration = config

    # метод __enter__ делает всю полезную работу с базой
    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionErr(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsErr

    # метод __exit__ закрывает соединение с базой
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
