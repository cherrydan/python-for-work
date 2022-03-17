# Уроки по ООП от selfedu.
# декораторы classmethod и staticmethod

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    # класс-метод всегда имеет ссылку на класс
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    # обычный метод
    def get_coord(self):
        return self.x, self.y

    # статический метод - применяется когда нужно создать просто сервисную функцию, БЕЗ ДОСТУПА к атрибутам осн.класса
    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(10, 20)
# обычному методу мы должны при вызове из базового класса указать параметр self
coords = Vector.get_coord(v)
print(*coords)
print(v.norm2(v.x, v.y))
