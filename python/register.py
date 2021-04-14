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


# Moet nog juiste gegevens
    db = mysql.connector.connect(
        user='root',
        password='Welkom01',
        host='172.17.0.3',
        database='pad')
    dbcursor = db.cursor()

    username = params.get('username', [''])[0]
    password = params.get('password', [''])[0]
    email = params.get('email', [''])[0]

    query = "SELECT username FROM Speler WHERE username='{fuser}'".format(fuser=username)
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    if result:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>registratie</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>Gebruikersnaan al in gebruik</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'
    else:
        query = "INSERT INTO pad.Speler (email,password,username) VALUES ('{femail}','{fpassword}','{fuser}')".format(femail=email, fpassword=password, fuser=username)
        dbcursor.execute(query)
        db.commit()
        db.close()
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>registratie</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>welkom</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    return [bytes(html, 'utf-8')]
