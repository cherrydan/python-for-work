from flask import request, render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from search_wlogin import app, db
from DBcm import *
from log_request import log_request
from search_wlogin.models import User
from vsearch import search4letters


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
    results = str(search4letters(phrase, letters))
    try:
        log_request(request, results)
    except Exception as err:
        flash('Logging failed with this error: ' + str(err))

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
@login_required
def view_the_log() -> str:
    """
    view_the_log()
    displays the log file into page
    :return: str
    """
    # cчитываем лог из БД, используя наш контекстный менеджер
    try:
        with UseDatabase(app.config['db_config']) as cursor:
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
    except ConnectionErr as err:
        str_ = 'Is your database switched on? Error! ' + str(err)
        return render_template('db_err.html', the_title=str_)
    except CredentialsErr as err:
        str_ = 'MySQL username or password is invalid! Error! ' + str(err)
        return render_template('db_err.html', the_title=str_)
    except Exception as err:
        str_ = 'Something else went wrong! ' + str(err)
        return render_template('db_err.html', the_title=str_)


# делает вход в систему, проверяя данные пользователя из базы
@app.route('/login', methods=['GET', 'POST'])
def do_login() -> 'html':
    login = request.form.get('login')
    password = request.form.get('password')
    # если данные из формы получены
    if login and password:

        user = User.query.filter_by(login=login).first()
        # пароль будем проверять по сравнению хэш-суммы
        if user and check_password_hash(user.password, password):
            login_user(user)  # если всё ок, логинизируем пользователя

            return redirect(url_for('view_the_log'))
        else:
            # если же не ок, выводим сообщение
            flash('Login or password is incorrect!')

    else:
        flash('Please, fill login and password fields!')
    return render_template('login.html', the_title='Login Form')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def do_logout() -> 'html':
    logout_user()
    return redirect(url_for('entry_page'))


# выводим форму регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    # TODO Adding user data to DB
    if request.method == 'POST':
        try:
            if not (login or password or password2):
                flash('Please, fill the registration form!')
            elif password != password2:
                flash('Passwords are not equal!')
            else:
                # хешируем пароль
                hash_pwd = generate_password_hash(password)
                new_user = User(login=login, password=hash_pwd)
                db.session.add(new_user)
                db.session.commit()

                return redirect(url_for('do_login'))
        except IntegrityError:
            flash('This login is already in use! Try another login!')

    return render_template('register.html', the_title='Registration Form')


# обработка 401-Unauthorized
@app.errorhandler(401)
def not_authorized(e):
    return render_template('e401.html', the_title='You are not authorized! ' +
                                                  'Please, use links below:')
