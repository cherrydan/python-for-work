from Iterators.HomeworkList import HomeworkList

arr = HomeworkList([1, 2, 3, 4, 5])  # создаём массив как экземпляр нашего класса, переопределенного от list
print('исходный массив: ', arr)

print(iter(arr))  # проверяем, будет ли он итерироваться нашим кастомным итератором (будет)
print('прокрученный через кастомный итератор массив: ')
for el in arr:
    print(el, end=' ')  # итерируем и любуемся на результат
