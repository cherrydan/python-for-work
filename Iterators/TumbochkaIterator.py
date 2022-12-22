class TumbochkaIterator:
    def __init__(self, some_obj):
        self.some_obj = some_obj
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.some_obj):
            result = self.some_obj[self.current]
            self.current += 1
            return result
        raise StopIteration
