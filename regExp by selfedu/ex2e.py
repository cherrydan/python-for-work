# Регулярные выражения by selfedu. Минорные квантификаторы. Разбор HTML-строки

import re

text = '<p>Картинка <img src="bg.jpg">в тексте </p>'

# будем выделять тег <img>

tmpl = r'<img.*>'  # жадный вариант

match = re.findall(tmpl, text)
print(match)  # Output: ['<img src="bg.jpg">в тексте </p>'] ложный результат

# минорный квантификатор
tmpl2 = r'<img.*?>'
match = re.findall(tmpl2, text)
print(match)  # Output: ['<img src="bg.jpg">'] ожидаемый результат
