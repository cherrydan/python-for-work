from jinja2 import Template

# создаём простой шаблон на jinja2
# впихиваем в него статические поля созданного класса Person,
# которые мы получаем при помощи геттеров
# внутри {{}} можно использовать любые выражения языка Python


class Person:
    def __init__(self, age, name):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name


per = Person(33, 'Фёдор')
tm = Template('Мне {{ p.getAge() }} лет и зовут меня {{ p.getName() }}')

msg = tm.render(p=per)
print(msg)
