from jinja2 import escape

# Уроки по шаблонизатору jinja2. Экранирование HTML-тегов на лету, при помощи класса escape

link = '''В HTML-документах ссылки определяются так:
<a href="#">Ссылка</a>
'''
print('Экранирование HTML-тегов при помощи класса escape\n')
msg = escape(link)
print(msg)