class Tumbochka:
    def __init__(self):
        self.boxes = {
            1: [],
            2: [],
            3: []
        }

    def add_to_box(self, obj, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            self.boxes[box_num].append(obj)

    def remove_from_box(self, box_num):
        if box_num not in {1, 2, 3}:
            print("Вы ввели неправильный номер ящика!")
        else:
            return self.boxes[box_num].pop()

    def __str__(self):
        boxes_items = self.boxes[1] + self.boxes[2] + self.boxes[3]
        return ", ".join(boxes_items)
