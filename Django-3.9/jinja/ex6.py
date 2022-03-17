# Уроки по jinja2. Наследование шаблонов. Именованные блоки.
from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render()
print(msg)