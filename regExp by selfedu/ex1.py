# Регулярные выражения by selfedu. Вводный пример

import re

text = 'Карта map и объект Bitmap - это разные вещи'

#  ищем где map - только отдельное слово
match = re.findall(r'\bmap\b', text)
print(match)