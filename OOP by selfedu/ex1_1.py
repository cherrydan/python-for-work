class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()
pt.set_coords(1, 2)

pt2 = Point()
pt2.set_coords(10, 20)

print(*pt.get_coords())
print(*pt2.get_coords())

