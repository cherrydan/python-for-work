from jinja2 import Template

# Уроки по jinja2. Фильтры и макросы. Использование фильтра в блоках {% filter %}

persons = [{'name': 'Николай', 'old': 18, 'weight': 78.5},
           {'name': 'Алексей', 'old': 28, 'weight': 82.3},
           {'name': 'Иван', 'old': 33, 'weight': 94.0},
           ]

tmpl = '''
{%- for person in persons -%}
{% filter upper %}{{person.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tmpl)
msg = tm.render(persons=persons)
print(msg)