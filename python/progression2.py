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

    query = "SELECT username FROM Speler WHERE username='{fusername}' AND password='{fpassword}'".format(fusername=username, fpassword=password)
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    if result:
        query2 = "SELECT `score_challenge2` FROM `pad`.`Score` WHERE `speler_id` = (SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fusername}' AND `password` = '{fpassword}') AND score_challenge2 IS NULL".format(fusername=username, fpassword=password)
        dbcursor.execute(query2)
        result2 = dbcursor.fetchall()
        if result2:
            query = "UPDATE `pad`.`Challenge` SET `stop_time` = CURRENT_TIMESTAMP() WHERE `speler_id` = (SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fusername}' AND `password` = '{fpassword}') AND challenge_id = 2".format(fusername=username, fpassword=password)
            dbcursor.execute(query)
            query2 = "UPDATE `pad`.`Score` SET `score_challenge2` = (SELECT TIMESTAMPDIFF (MINUTE, `start_time`, `stop_time`) FROM `pad`.`Challenge` WHERE `challenge_id` = 2 AND  `speler_id` = (SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fusername}' AND `password` = '{fpassword}')) WHERE `speler_id` = (SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fusername}' AND `password` = '{fpassword}')".format(fusername=username, fpassword=password)
            dbcursor.execute(query2)
            db.commit()
            db.close()
            html = ''
            html += '<html>\n'
            html += ' <head>\n'
            html += '  <title>registratie</title>\n'
            html += ' </head>\n'
            html += ' <body>\n'
            html += '  <h1>Score</h1>\n'
            html += ' </body>\n'
            html += '</html>\n'

        else:
            html = ''
            html += '<html>\n'
            html += ' <head>\n'
            html += '  <title>Progression</title>\n'
            html += ' </head>\n'
            html += ' <body>\n'
            html += '  <h1>you already completed this challenge!</h1>\n'
            html += ' </body>\n'
            html += '</html>\n'

    else:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Progression</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>Inlog fout!</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    return [bytes(html, 'utf-8')]
