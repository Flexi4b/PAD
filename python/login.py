# nog methods importeren

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
    host="localhost",
    user="PAD",
    password="IC103A",
    database="PAD"
    )
    dbcursor = db.cursor()

    username = params.get('userid', [''])[0]
    password = params.get('password', [''])[0]

    query = "SELECT username FROM PAD WHERE username='{fuser}' AND password='{fpassword}'".format(fuser = username, fpassword = password)
    dbcursor.execute(query)
    result = dbcursor.fetchall()

    if result:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Login</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>inloggen gelukt</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'
    else:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Login</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>onjuist wachtwoord en/of gebruikersnaam</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    return [bytes(html, 'utf-8')]