import urllib.parse as urlparse
import mysql.connector


def application(environ, start_response):
    status = '200 OK'
    response_header = [('Content-type', 'text/html')]
    start_response(status, response_header)

    method = environ.get('REQUEST_METHOD', '')

    params = {}
    if method == 'GET':
        params = urlparse.parse_qs(environ['QUERY_STRING'])
    elif method == 'POST':
        input = environ['wsgi.input'].read().decode()
        params = urlparse.parse_qs(input)

    db = mysql.connector.connect(
        user='root',
        password='Welkom01',
        host='172.17.0.3',
        database='pad')

    username = params.get('username', [''])[0]
    password = params.get('password', [''])[0]
    email = params.get('email', [''])[0]

    sql_insert_data = "INSERT INTO `pad`.`Speler` (`username`, `password`, `email`) VALUES ('{}', '{}', '{}')".format(username, password, email)

    cursor = db.cursor()
    cursor.execute(sql_insert_data)
    db.commit()
    cursor.close()
    db.close()
