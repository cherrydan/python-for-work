class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def __del__(self):
        print('Вызов метода __del__')


pt = Point()
print(pt.__dict__)

pt2 = Point(10, 20)
print(pt2.__dict__)
