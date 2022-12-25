from Iterators.HomeworkIterator import HomeworkIterator
# для того, чтобы воспользоваться нашим кастомным итератором нам надо
# отнаследоваться от стандартного класса list


class HomeworkList(list):
    def __init__(self, value):
        self.value = value  # инициализируем значение
        super().__init__(self.value)  # вызываем конструктор суперкласса

    def __iter__(self):  # в переопределённом методе __iter__ пропихиваем наш кастомный итератор
        return HomeworkIterator(self.value)

    def __str__(self):  # переопределяем этот метод, чтобы наши значения могли выводиться
        return str(self.value)
