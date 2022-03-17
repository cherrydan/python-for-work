from jinja2 import Template, FileSystemLoader, Environment

# Уроки по jinja2. Загрузка шаблонов. Загрузка шаблона из папки файловой системы
# (FileSystemLoader)

persons = [{'name': 'Николай', 'old': 18, 'weight': 78.5},
          {'name': 'Алексей', 'old': 28, 'weight': 82.3},
          {'name': 'Иван', 'old': 33, 'weight': 94.0},
          ]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)
print(msg)