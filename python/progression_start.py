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
        query = "INSERT INTO `pad`.`Challenge1` (`speler_id`,`start_time`) VALUES ((SELECT `speler_id` FROM `pad`.`Speler` WHERE `username` = '{fuser}' AND `password` = '{fpassword}'), CURRENT_TIMESTAMP())".format(fuser=username, fpassword=password)
        dbcursor.execute(query)
        db.commit()
        db.close()
        html = ''
        html += '<!DOCTYPE html> \n'
        html += '<html lang="en"> \n'
        html += '<head> \n'
        html += '    <meta charset="UTF-8"> \n'
        html += '    <meta name="viewport" content="width=device-width, initial-scale=1.0"> \n'
        html += '    <link rel="stylesheet" type="text/css" href="../css/challenge1.css" /> \n'
        html += '    <link rel="preconnect" href="https://fonts.gstatic.com"> \n'
        html += '    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">  \n'
        html += '</head> \n'
        html += '<body> \n'
        html += '    <div id="container"> \n'
        html += '        <header> \n'
        html += '            <h1>Linda`s food blog < / h1 > \n'
        html += '        </header> \n'
        html += '         \n'
        html += '         \n'
        html += '        <div class="row"> \n'
        html += '            <main class="leftcolumn"> \n'
        html += '                <div class="card"> \n'
        html += '                    <h2 class="datum">15/02/2018 Banaan- en aardbeiensmoothie</h2> \n'
        html += '                    <p> \n'
        html += '                        Goedendag en welkom bij mijn blog! <br> Het is vandaag 15 februari 2018 en ik heb een verrukkelijk smoothie recept dat ik met jullie wil delen,  \n'
        html += '                        het is een banaan- en aardbeiensmoothie! Hier volgen de ingrdiënten en de bereidingswijze die je nodig zal hebben om het recept te maken. \n'
        html += '                    </p> \n'
        html += '                    <hr> \n'
        html += '                    <h4>Ingrediënten (4 smoothies):</h4> \n'
        html += '                    <p>4 rijpe bananen</p> \n'
        html += '                    <p>250 gr. aardbeien</p> \n'
        html += '                    <p>300 ml melk</p> \n'
        html += '                    <p> 300 ml. yoghurt</p> \n'
        html += '                    <p>scheutje vloeibare honing</p> \n'
        html += '                    <p>4 tl. lijnzaad</p> \n'
        html += '                    <p>4 el. havervlokken</p> \n'
        html += '                    <hr> \n'
        html += '                    <img src="../Photo/banaan- en aardbeismoothie.jpg" alt="Banaan en aardbeismoothie"> \n'
        html += '                    <h4>Bereidingswijze:</h4> \n'
        html += '                    <p>Pel de bananen en snij deze in plakken. Haal de kroontjes van de aardbeien en halveer eventueel de grootste aardbeien. Doe de aardbeien en stukken banaan in een blender en voeg hier de melk en de yoghurt aan toe.</p> \n'
        html += '                    <p>Doe het lijnzaad en de havervlokken erbij en doe er naar smaak wat vloeibare honing (of vanillesuiker) bij. Als je de smoothie als ontbijtsmoothie neemt kan je flink wat extra havermout toevoegen, gebruik dan 250 ml. yoghurt en 350 ml. melk.</p> \n'
        html += '                    <p>Pureer het geheel in je blender tot een romige smoothie. Laat de snelheid van de blender eerst oplopen en daarna weer aflopen, of gebruik de smoothiestand als je blender dit heeft. Heb je geen blender dan kan je deze smoothie ook met een staafmixer maken.</p> \n'
        html += '                    <p>Tip: voeg een paar bolletjes vanilleijs toe of laat de banaan vantevoren in de vriezer afkoelen. Zo krijg je een soort milkshake, heerlijk op een warme dag.</p> \n'
        html += ' \n'
        html += '                     \n'
        html += '                     \n'
        html += '                     \n'
        html += '                </div> \n'
        html += '            </main> \n'
        html += '            <div class="rightcolumn"> \n'
        html += '                <div class="card"> \n'
        html += '                    <h2>About Me</h2> \n'
        html += '                    <img src="../Photo/blog-schrijver.jpg" alt="blog-schrijver"> \n'
        html += '                    <p>blablalab wat ben k een goeie kok</p> \n'
        html += '                </div> \n'
        html += '                <nav class="card"> \n'
        html += '                    <h3>Navigatie</h3> \n'
        html += '                    <ul class="links"> \n'
        html += '                        <li><a class="selected" href="#">Startpagina</a></li> \n'
        html += '                        <br> \n'
        html += '                        <li><a class="selected" href="#">Login</a></li> \n'
        html += '                        <br> \n'
        html += '                        <li><a class="selected" href="#">Andere recepten</a></li> \n'
        html += '                        <br> \n'
        html += '                        <li><a class="selected" href="#">Contact</a></li> \n'
        html += '                        <br> \n'
        html += '                        <li><a class="selected" href="#">Hints</a></li> \n'
        html += '                    </ul> \n'
        html += '                </nav> \n'
        html += '            </div> \n'
        html += '        </div> \n'
        html += '        <footer> \n'
        html += '            <h3>Copyright &copy; 2021 Linda`s foodblog </h3> \n'
        html += '            <a class="admin" href="../html/admin.html">Admin</a> \n'
        html += '        </footer> \n'
        html += ' \n'
        html += '    </div> \n'
        html += '</body> \n'
        html += '</html> \n'
        html += ' \n'

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
