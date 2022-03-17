from jinja2 import Template

# Уроки по jinja2. Фильтры и макросы. Фильтр random

cars = [{'model': 'Audi', 'price': 23000},
        {'model': 'Skoda', 'price': 17300},
        {'model': 'Volvo', 'price': 44300},
        {'model': 'VW', 'price': 21300}]

tmpl = 'Случайно выбранный автомобиль {{cars | random }}'
tm = Template(tmpl)
msg = tm.render(cars=cars)

print(msg)
