# Регулярные выражения by selfedu. Квантификаторы. Краткая форма записи.
import re

text = 'Google, Gooogle, Goooooogle!'

# будем искать в шаблоне, где буква 'o' в слове Gogle встречается 2 или более раз
tmpl = r'Go{2,}gle'

match = re.findall(tmpl, text)
print(match) # Output: ['Google', 'Gooogle', 'Goooooogle']

# где буква 'o' будет встречаться не более 4-х раз
tmpl = r'Go{,4}gle'
match = re.findall(tmpl, text)
print(match) # Output: ['Google', 'Gooogle']

