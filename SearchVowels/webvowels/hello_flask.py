# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session
from config import *
from checker import check_logged_in
from quicksession.secret import *

import vsearch

from DBcm import *

app = Flask(__name__)

app.config['dbconfig'] = {
    'host': HOST,
    'user': USER,
    'password': PASSWORD,
    'database': DATABASE,
}


def log_request(req: 'flask_request', res: str) -> None:
    """
    log_request(req, res)
    writes requested url and result of vowels-search to log-file
    :param req: flask-requested URL
    :param res: result string with vowels
    :return: None
    Journalize data into MySql-table
    """

    # подключаемся к классу-контекстному менеджеру UseDatabase
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """INSERT INTO log
        (phrase, letters, ip, browser_string, results)
        values(%s, %s, %s, %s, %s)
        """
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res,
                              )
                       )


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    """
    do_search() - > str
    doing vowels search
    :return: str with wowels were found
    """
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here is your results: '
    results = str(vsearch.search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """
    entry_page()
    displays entry page via Jinja2
    :return: any htlm data
    """
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the Web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> str:
    """
    view_the_log()
    displays the log file into page
    :return: str
    """
    # cчитываем лог из БД, используя наш контекстный менеджер
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """ SELECT phrase, letters, ip, browser_string, results 
        FROM log
        """
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    # и шаблонизируем
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,
                           )


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


if __name__ == '__main__':
    app.secret_key = SECRET_KEY
    app.run(debug=True)
