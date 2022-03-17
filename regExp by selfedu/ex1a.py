# Регулярные выражения by selfedu. символьные классы
import re

text = 'Еда, беду, победа'

tmpl = r'[еЕ]д[ау]'  # этот шаблон нам говорит, что первая буква может быть Е малое или большое, потом д
# а последняя буква либо а либо у

match = re.findall(tmpl, text)

print(match)

# ищем при помощи символьного класса, две цифры подряд от 0 до 9

tmpl = r'[0-9][0-9]'

text = '374 69 38'

match = re.findall(tmpl, text)
print(match)  # output: 37 69 38

text = 'Еда, беду, -5 55 победа'
tmpl = r'[^0-9]' # ^ означает инвертирование значения шаблона - т.е. здесь будем искать НЕ ЦИФРЫ
match = re.findall(tmpl, text)
print(match)

# изменим шаблон, прямо зададим диапазон букв для поиска
tmpl = r"[a-я]" # будут найдены только маленькие буквы от a до я
match = re.findall(tmpl, text)
print(match)

tmpl = r'\d'
match = re.findall(tmpl, text)
print(match)