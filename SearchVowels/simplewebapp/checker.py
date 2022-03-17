# -*- coding: utf-8 -*-

"""
Модуль, в котором мы создаём декорируемую функцию, проверяющую вошел ли пользователь в систему
"""
from flask import session, render_template
from functools import wraps


def check_logged_in(func):
    # функция-обёртка
    @wraps(func)
    def wrapper(*args, **kwargs) -> 'html':
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return render_template('login.html', the_title='Please, log in!',
                               the_message='This content for register users only!')
    return wrapper


