from jinja2 import Template

# Уроки по jinja2. Фильтры и макросы. Фильтр sum, max, min

cars = [{'model': 'Audi', 'price': 23000},
        {'model': 'Skoda', 'price': 17300},
        {'model': 'Volvo', 'price': 44300},
        {'model': 'VW', 'price': 21300}]

tmpl = "Суммарная стоимость автомобилей {{ cars | sum(attribute='price')}}"
tm = Template(tmpl)
msg = tm.render(cars=cars)

print(msg)

tmpl = """Самый дорогой автомобиль в списке: {{ (cars | max(attribute='price')).model}}
Его стоимость: {{(cars | max(attribute='price')).price}} USD"""

tm = Template(tmpl)
msg = tm.render(cars=cars)
print(msg)


tmpl = """Самый дешевый автомобиль в списке: {{ (cars | min(attribute='price')).model}}
Его стоимость: {{(cars | min(attribute='price')).price}} USD"""

tm = Template(tmpl)
msg = tm.render(cars=cars)
print(msg)

