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

    query = "SELECT username FROM Speler WHERE username='{fuser}'".format(fuser=username)
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    if result:
        query = "UPDATE `pad`.`Challenge1` SET `stop_time` = CURRENT_TIMESTAMP() WHERE `speler_id` = (SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fuser}' AND `password` = '{fpassword}')".format(fuser=username, fpassword=password)
        query2 = "INSERT INTO `pad`.`Score` (`speler_id`, `score_challenge1`) VALUES ((SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fuser}' AND `password` = '{fpassword}'), (SELECT TIMESTAMPDIFF (MINUTE, `start_time`, `stop_time`) FROM `pad`.`Challenge1` WHERE `speler_id` = (SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fuser}' AND `password` = '{fpassword}')))" .format(fuser=username, fpassword=password)
        dbcursor.execute(query)
        dbcursor.execute(query2)
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

    else:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Progression</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>Inlog fout</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    return [bytes(html, 'utf-8')]
