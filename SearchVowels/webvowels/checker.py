# -*- coding: utf-8 -*-

"""
Модуль, в котором мы создаём декорируемую функцию, проверяющую вошел ли пользователь в систему
"""
from flask import session
from functools import wraps


def check_logged_in(func):
    # функция-обёртка
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return "<font color=red><h2>This content is for register users only</font></h2>"
    return wrapper


