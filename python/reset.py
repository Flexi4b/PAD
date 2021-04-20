import random
import string
import smtplib
import urllib.parse as urlparse
import mysql.connector


source = string.ascii_letters + string.digits
newPassword = ''.join((random.choice(source) for i in range(8)))


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


    fromx = 'syscribe@gmail.com'
    mail = params.get('email', [''])[0]
    subject = 'Password'
    msg = 'Subject:{}\n\nDont forget your password pipo.\nHere is a new one:\n{}\n'.format(subject, newPassword)

    db = mysql.connector.connect(
        user='root',
        password='Welkom01',
        host='172.17.0.3',
        database='pad')
    dbcursor = db.cursor()

    query = "SELECT email FROM Speler WHERE email='{}'".format(mail)
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    if result:
        query = "update pad.Speler set password = '{}' where email = '{}';".format(newPassword, mail)
        dbcursor.execute(query)
        db.commit()
        db.close()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login('syscribe@gmail.com', 'Hacker420')
        server.sendmail(fromx, mail, msg)
        server.quit()

        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Reset</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>Mail verstuurd</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    else:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Reset</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>Geen account met deze mail</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    return [bytes(html, 'utf-8')]
