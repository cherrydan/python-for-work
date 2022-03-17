from jinja2 import Template

# Уроки по шаблонизатору jinja2. Используем if, elif и else в шаблоне

cities = [{'id': 1, 'city':  'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}
          ]
# тег HTML select - это такой выпадающий список
link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
        <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == 'Москва' -%}
    <option>Столица нашей Родины  - Москва!</option>
{% else -%}
{{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)



