# Уроки по jinja2. Загрузка шаблонов. Конструкция include
from jinja2 import FileSystemLoader, Environment

persons = [{'name': 'Николай', 'old': 18, 'weight': 78.5},
          {'name': 'Алексей', 'old': 28, 'weight': 82.3},
          {'name': 'Иван', 'old': 33, 'weight': 94.0},
          ]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='https://mail.ru', title='Про Jinja')
print(msg)