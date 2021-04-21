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
        query2 = "SELECT speler_id FROM Challenge WHERE speler_id = (SELECT speler_id FROM Speler WHERE username = '{fusername}' AND password = '{fpassword}')".format(fusername=username, fpassword=password)
        dbcursor.execute(query2)
        result2 = dbcursor.fetchall()
        if result2:
            html = ''
            html += '<html>\n'
            html += ' <head>\n'
            html += '  <title>Progression</title>\n'
            html += ' </head>\n'
            html += ' <body>\n'
            html += '  <h1>you have to complete challenge 1 first</h1>\n'
            html += ' </body>\n'
            html += '</html>\n'

        else:
            query3 = "INSERT INTO `pad`.`Challenge` (`speler_id`,`start_time`,`challenge_id`) VALUES ((SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fuser}' AND `password` = '{fpassword}'), CURRENT_TIMESTAMP(), '2')".format(fuser=username, fpassword=password)
            dbcursor.execute(query3)
            db.commit()
            db.close()
            html = ''
            html += '<!DOCTYPE html>\n'
            html += '\n'
            html += '<html>\n'
            html += '<head>\n'
            html += '    <!-- Hier koppel ik mijn index aan het CSS zodat elke pagina er hetzelfde uitziet-->\n'
            html += '    <link rel="stylesheet" href="../../css/challenge2.css">\n'
            html += '</head>\n'
            html += '<body>\n'
            html += '    <!--Bij elke div geef je er een naam aan zodat je het in het css kan stylen naar wens, zoals hier titel staat-->\n'
            html += '    <div class="titel">\n'
            html += '        <h1>CRYPTOB4NK</h1> <!-- Hier zie je mijn header waar de bedrijfsnaam staat -->\n'
            html += '    </div>\n'
            html += '\n'
            html += '    <div>\n'
            html += '\n'
            html += '        <div class="menu">\n'
            html += '            <!--Dit staat voor mijn snelkoppeling menu aan de zijkant om te navigeren tussen pagina`s -->\n'
            html += '            <a class= "selected" href="../html/challenge1/cryptobank.html">Home</a><hr> <!-- Hier link ik dus naar andere html bestanden en geef ik een display naam-->\n'
            html += '            <a class= "selected" href="../html/challenge1/banklogin.html">Inloggen</a><hr> <!-- Hier link ik dus naar andere html bestanden en geef ik een display naam-->\n'
            html += '        </div>\n'
            html += '\n'
            html += '        <div class="hoofdtekst">\n'
            html += '            <!--Bij elke div geef je er een naam aan zodat je het in het css kan stylen naar wens, zoals hier mijn hoofdtekst staat-->\n'
            html += '            <h2>CRYPTOB4NK de bank voor jou bitcoins.</h2> <!-- Hier zie je mijn 2de header waar staat waar deze pagina over gaat -->\n'
            html += '            <p>\n'
            html += '                Real-time overzicht van de ontwikkelingen betreft de bitcoin:<!-- Een stuk tekst op de pagina -->\n'
            html += '            </p>\n'
            html += '            <div style="height:560px; background-color: #FFFFFF; overflow:hidden; box-sizing: border-box; border: 1px solid #56667F;\n'
            html += '             border-radius: 4px; text-align: right; line-height:14px; font-size: 12px; font-feature-settings: normal; text-size-adjust: 100%; box-shadow: inset 0 -20px 0 0 \n'
            html += '             #56667F;padding:1px;padding: 0px; margin: 0px; width: 100%;"><div style="height:540px; padding:0px; margin:0px; width: 100%;">\n'
            html += '             <iframe src="https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=859&pref_coin_id=1505" width="100%" height="536px" scrolling="auto" marginwidth="0" marginheight="0" \n'
            html += '             frameborder="0" border="0" style="border:0;margin:0;padding:0;line-height:14px;"></iframe></div><div style="color: #FFFFFF; line-height: 14px; font-weight: 400; font-size: 11px; box-sizing: border-box; \n'
            html += '             padding: 2px 6px; width: 100%; font-family: Verdana, Tahoma, Arial, sans-serif;"><a href="https://coinlib.io" target="_blank" style="font-weight: 500; color: #FFFFFF; text-decoration:none; font-size:11px">\n'
            html += '             Cryptocurrency Prices</a>&nbsp;by Coinlib</div></div> <!--Widget die bitcoin bijhoud-->\n'
            html += '        </div>\n'
            html += '\n'
            html += '\n'
            html += '        <div class="contact">\n'
            html += '            <!--Hier staat het contact kopje voor als klanten directe comminucatie willen-->\n'
            html += '            <h2>Te bereiken via:</h2> <!--Weer een header die de informatie inleid-->\n'
            html += '            <a href="mailto:info@cryptobank.com">Contact via mail</a> <!--Een link naar het mailadres, waardoor je direct een mail opstelt-->\n'
            html += '\n'
            html += '\n'
            html += '\n'
            html += '\n'
            html += '            <p><a href="tel:020-64042190">Contact via telefoon</a></p> <!--Een link naar het telefoonnummer waardoor je meteen zou kunnen bellen of het nummer kan achterhalen-->\n'
            html += '            <a>Lammonggracht 21 Amsterdam 1019RD </a> <!--Adres-->\n'
            html += '        </div>\n'
            html += '    </div>\n'

    else:
        html = ''
        html += '<html>\n'
        html += ' <head>\n'
        html += '  <title>Progression</title>\n'
        html += ' </head>\n'
        html += ' <body>\n'
        html += '  <h1>Inlog fout!!!!</h1>\n'
        html += ' </body>\n'
        html += '</html>\n'

    return [bytes(html, 'utf-8')]
