# уроки по ООП от selfedu
# механизм инкапсуляции

class Point:
    # protected (_) атрибуты де-факто никак не ограничены в доступе
    # поэтому их лучше использовать для пометки только служебных переменных

    # ограничиваются в доступе реально только private (__) атрибуты

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами!')

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        # делаем перед присваиванием проверку на тип
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами!')

    def get_coord(self):
        return self.__x, self.__y


pt = Point(10, 20)
print(*pt.get_coord())
pt.set_coord(200, 300)
print(*pt.get_coord())
