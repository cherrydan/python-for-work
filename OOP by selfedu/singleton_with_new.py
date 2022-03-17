# Уроки selfedu по ООП.
# Реализация паттерна singleton при помощи вызова магического метода __new__
# он немножко недоделанный ну да ладно.
# (с) selfedu
from docutils.parsers.rst.directives.admonitions import Danger


class DataBase:
    __instance = None

    # магический метод __new__ получает в качестве параметра экземпляр класса
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # передаём адрес экземпляра класса
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # вот тут обязательно в методе-финализаторе нужно вернуть значение __instance в None
    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, pswrd, port):
        self.user = user
        self.pswrd = pswrd
        self.port = port

    def connect(self):
        print(f'Соединение с БД: user {self.user} port {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'данные'

    def write(self, data):
        print(f'Запись данных в БД {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '3456', 8080)

print(id(db), id(db2))

db.connect()
db2.connect()
