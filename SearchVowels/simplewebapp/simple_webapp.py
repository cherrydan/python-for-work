#!/usr/bin/python3
# -*- coding: utf-8 -*-

from quicksession.secret import *
from flask import Flask, session
from checker import check_logged_in
"""

Простое приложение на три урла,
переходить на которые мы будем разрешать только авторизованым пользователям

"""
app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "<h1>Hello from simple webapp</h1>"


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return """<h1> <font color="red">Page1</font></h1>"""


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return """<h1> <font color="green">Page2</font></h1>"""


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return """<h1> <font color="blue">Page3</font></h1>"""


# делает вход в систему, присваивая ключу logged_in из словаря session значение
@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return "<h2>You are logged in!</h2>"


# уничтожает ключ logged_in в словаре session
@app.route('/logout')
def do_logout() -> str:
    try:
        session.pop('logged_in')
        return "<h2>You are now logged out!<h2>"
    except KeyError:
        return "<h2>Key Error: key 'logged_in' doesn't exist!</h2>\nDo log in!"


# проверяем статус ключа logged_in
@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return """<h2><font color="green">You are currently logged in!</font><h2>"""
    else:
        return """<h2><font color="red">You are NOT logged in!</font><h2>"""


app.secret_key = SECRET_KEY

if __name__ == '__main__':
    app.run(debug=True)
