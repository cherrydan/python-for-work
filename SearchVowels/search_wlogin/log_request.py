from DBcm import *
from search_wlogin import app


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
    with UseDatabase(app.config['db_config']) as cursor:
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
