class HomeworkIterator:
    # наш кастомный итератор должен при проходке к входящему значению добавлять 10 единиц
    def __init__(self, some_obj):
        self.counter = 0
        self.some_obj = some_obj

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.counter < len(self.some_obj):
                result = self.some_obj[self.counter] + 10 # здесь мы берём текущее значение и прибавляем к нему 10
                self.counter += 1  # пока не достигнут конец массива передвигаем счётчик
                return result  # возвращаем новое значение
            raise StopIteration
        except TypeError:
            print('Исходный массив должен состоять из чисел, не строк')
            raise StopIteration
