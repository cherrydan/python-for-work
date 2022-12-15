tumb = ['ножницы', 'карандаш', 'яблоко', 'книга']

it = iter(tumb)

try:
    while True:
        next_val = next(it)
        print('Значение: ', next_val)
except StopIteration:
    print('Перебор закончен')

print('Программа завершена')