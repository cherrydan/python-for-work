#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Простое приложение, позволяющее сохранять и получать данные из сессии
Flask
"""
from flask import Flask, session
from secret import *

app = Flask(__name__)

# сохраняем секретный ключ
app.secret_key = SECRET_KEY


@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    """
    setuser(user)
    sets the user parameter from url-string to session cookie

    :param user: string
    :return: string with user name
    """
    session['user'] = user
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    """
    getuser()
    gets user name from session cookie
    :return: string
    """
    return 'User value currently is : ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
