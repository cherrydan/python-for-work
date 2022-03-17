from jinja2 import Template

# уроки по jinja2. Блоки экранированных символов (raw)

data = '''Модуль jinja, 
вместо определения {{name}},
подставляет соответствующее
значение.
'''

tm = Template(data)
msg = tm.render(name='Фёдор')
print(msg)

print()
rawdata = '''{% raw %}Модуль jinja, 
вместо определения {{name}},
подставляет соответствующее
значение.{% endraw %}
'''
tm = Template(rawdata)
msg = tm.render(name='Фёдор')
print(msg)
