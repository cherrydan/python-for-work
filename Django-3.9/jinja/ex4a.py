from jinja2 import Template, FunctionLoader, Environment

# Уроки по jinja2. Загрузка шаблонов. Загрузка шаблона через написанную функцию
# (FunctionLoader)

persons = [{'name': 'Николай', 'old': 18, 'weight': 78.5},
           {'name': 'Алексей', 'old': 28, 'weight': 82.3},
           {'name': 'Иван', 'old': 33, 'weight': 94.0},
           ]


def load_tmpl(path):
    if path == 'index':
        return 'Имя {{ u.name }}'
    elif path == 'index2':
        return 'Имя {{ u.name }}, Возраст {{ u.old }}'
    else:
        return 'Данные {{ u }}'


func_loader = FunctionLoader(load_tmpl)
env = Environment(loader=func_loader)
tm = env.get_template('index2')
msg = tm.render(u=persons[0])
print(msg)