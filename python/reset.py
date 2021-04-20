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


    mailFrom = 'syscribe@gmail.com'
    mailTo = params.get('email', [''])[0]
    subject = 'Password'
    msg = 'Subject:{}\n\nDont forget your password anymore pipo.\nHere is a new one:\n{}'.format(subject, newPassword)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login('syscribe@gmail.com', 'Hacker420')
    print("login gelukt")
    server.sendmail(mailFrom, mailTo, msg)
    print("mail verstuurd")
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

    return [bytes(html, 'utf-8')]
