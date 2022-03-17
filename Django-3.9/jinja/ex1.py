from jinja2 import Template

# создаём простой шаблон на jinja2
# впихиваем в шаблон простые переменные, взятые с консоли у пользователя

name = input('Введите Ваше имя -> ')

tm = Template('Привет, {{ name }}!')
msg = tm.render(name=name)

age = int(input('Введите Ваш возраст -> '))

tm2 = Template('Меня зовут {{n}} и мне {{a}} лет.')

# здесь именнованые параметры ведут себя как словарь с любыми парами ключ-значение
msg2 = tm2.render(a=age, n=name)

print(msg)
print(msg2)



