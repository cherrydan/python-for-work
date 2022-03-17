from jinja2 import Template

# создаём простой шаблон на jinja2
# и впихиваем в него просто напросто словарь по ключу

person = {'name': 'Фёдор', 'age': 29}

tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name']}}.")
msg = tm.render(p=person)

print(msg)