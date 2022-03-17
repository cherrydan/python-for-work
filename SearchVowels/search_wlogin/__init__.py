#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Здесь я буду пытаться создать Flask-login
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import *
from search_wlogin.DBcm import ConnectionErr, CredentialsErr

from secret.secret import *

app = Flask(__name__)

app.config['db_config'] = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}

# данными пользователей будем управлять через ORM SQLAlchemy
# настраиваем доступ к базе
str_ = 'mysql://' + 'vsearch' + ':' + 'Vsearchpasswd21' + '@' + 'localhost' + '/' + 'vsearchlogDB'
app.config['SQLALCHEMY_DATABASE_URI'] = str_
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = SECRET_KEY


db = SQLAlchemy(app)
# создаём переменную менеджера логинов
manager = LoginManager(app)

# доступаемся до базы при помощи SQLAlchemy
db.create_all()



