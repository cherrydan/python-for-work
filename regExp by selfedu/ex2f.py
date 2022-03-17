# Регулярные выражения by selfedu. Правильное распарсивание тега img

import re

text = '<p>Картинка <img alt="картинка" src ="bg.jpg">в тексте </p>'

# будем выделять тег <img src ...>

tmpl2 = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
match = re.findall(tmpl2, text)
print(match)  # Output:
