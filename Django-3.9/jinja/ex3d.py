from jinja2 import Template

# Уроки по jinja2. Фильтры и макросы. Вложенные макросы, {% call %}

persons = [{'name': 'Николай', 'old': 18, 'weight': 78.5},
           {'name': 'Алексей', 'old': 28, 'weight': 82.3},
           {'name': 'Иван', 'old': 33, 'weight': 94.0},
           ]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{ caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
<ul>
<li>age: {{ user.old }}
<li>weight: {{ user.weight }}
</ul>
{% endcall %}

'''

tm = Template(html)
msg = tm.render(users=persons)
print(msg)