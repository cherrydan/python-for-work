from jinja2 import Template

# работа с шаблонизатором jinja2. Экранирование тегов HTML

link = '''В HTML-документах ссылки определяются так:
<a href="#">Ссылка</a>
'''
tm = Template(link)
msg = tm.render()
print(msg)

# делаем escape-команду при помощи символа |
tm = Template("{{ link | e }}")
msg = tm.render(link=link)
print()
print(msg)