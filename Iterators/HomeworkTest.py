from Iterators.HomeworkList import HomeworkList

arr = HomeworkList([1, 2, 3, 4, 5])  # создаём массив как экземпляр нашего класса, переопределенного от list
print('исходный массив: ', arr)

print(iter(arr))  # проверяем, будет ли он итерироваться нашим кастомным итератором (будет)
print('прокрученный через кастомный итератор массив: ')
for el in arr:
    print(el, end=' ')  # итерируем и любуемся на результат

print()

print('Прокрутим массив вещественных чисел: ')
arr2 = HomeworkList([
    25.43, 546.54, 768.6
])
print(arr2)
for el in arr2:
    print(el, end=' ')  # итерируем и любуемся на результат
