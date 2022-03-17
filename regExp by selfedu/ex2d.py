# Регулярные выражения by selfedu. Квантификаторы. Парсинг довольно сложной строки
import re

text = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001'

tmpl = r'\w+\s*=\s*[^;]+'  # выделяем все слова, кроме ;

match = re.findall(tmpl, text)
print(match)  # Output: ['author=Пушкин А.С.', 'title = Евгений Онегин', 'price =200', 'year= 2001']
