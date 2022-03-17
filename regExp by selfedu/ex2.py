# Регулярные выражения by selfedu. Квантификаторы. Мажорный и минорный режимы.
import re
text = 'Google, Gooogle, Goooooogle!'

# шаблон поиска с квантификатором - определяем сколько раз (!) встречается заданный символ
# (мажорный режим)
tmpl = r'o{2,5}'

match = re.findall(tmpl, text)
print(match)

# минорный режим, выводит только по минимальному количеству искомых символов в запросе - то есть по 3

tmpl = r'o{3,5}?'
match = re.findall(tmpl, text)
print(match) # Output: ooo (from second word), ooo, ooo (from third word - 6 symbols 'o' extracted to 2 tuplets)

