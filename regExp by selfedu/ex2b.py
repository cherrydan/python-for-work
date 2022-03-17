# Регулярные выражения by selfedu. Квантификаторы. Пример с номером телефона
import re

# 8 и далее 10 цифр (любых)
phone = '89123456789'
phone2 = '7827362'
tmpl = r'8\d{10}'

match = re.findall(tmpl, phone)
print(match)

# скормим неправильный номер, не по шаблону
# match = re.findall(tmpl, phone2)
# print(match) # Output: [] (пустой список)

if len(match) != 0:
    print('Номер телефона корректен')
else:
    print('Номер телефона некорректен!')