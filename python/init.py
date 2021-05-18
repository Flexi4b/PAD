from flask import Flask, render_template, request, session, redirect, url_for
from flaskext.mysql import MySQL
import smtplib
from email.message import EmailMessage
import random
import string

app=Flask(__name__)
app.secret_key = 'Hacker420'

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Welkom01'
app.config['MYSQL_DATABASE_DB'] = 'pad'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.3'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

display = []

@app.route('/')
def home():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if session.get('loggedin') == True:
        return redirect(url_for('welkom'))
    return render_template('index.html')

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if session.get('loggedin') == True:
        return redirect(url_for('welkom'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor.execute('SELECT * FROM Speler WHERE username = %s AND password = %s', (username, password,))
        user = cursor.fetchone()
        if user:
            if not display:
               display.append(username)
            display.clear()
            display.append(username)
            cursor.execute('SELECT speler_id FROM Speler WHERE username = %s', (username))
            id = cursor.fetchone()
            session['loggedin'] = True
            session['id'] = id
            session['username'] = username
            return redirect(url_for('welkom'))
        else:
            return render_template("login.html", msg = 'Incorrect username/password!')
    return render_template("login.html")

@app.route('/logout')
def logout():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if session.get('loggedin') == True:
        return redirect(url_for('welkom'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor.execute('SELECT username FROM Speler WHERE username = %s', (username))
        result = cursor.fetchone()
        if result:
            return render_template("register.html", msg='Username is taken. Try another.')
        source = string.ascii_letters + string.digits
        code = ''.join((random.choice(source) for i in range(8)))
        create = cursor.execute('insert into Speler (`username`, `password`, `email`, `code`) values (%s, %s, %s, %s)', (username, password, email, code))
        conn.commit()
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/forget', methods=['GET', 'POST'])
def forget():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if session.get('loggedin') == True:
        return redirect(url_for('welkom'))
    if request.method == 'POST' and 'email' in request.form:
        email = request.form['email']
        cursor.execute('SELECT email FROM Speler WHERE email = %s', (email))
        result = cursor.fetchone()
        if result:
            source = string.ascii_letters + string.digits
            code = ''.join((random.choice(source) for i in range(8)))
            update = cursor.execute('update Speler set code = %s where email = %s;', (code, email))
            conn.commit()
            email = email = request.form['email']
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login('syscribe@gmail.com', 'Hacker420')
            msg = EmailMessage()
            bericht = "here is a code to reset your passwoord: {}".format(code)
            msg.set_content(bericht)
            msg['Subject'] = 'password'
            msg['From'] = 'Syscribe no-reply <syscribe@gmail.com>'
            msg['To'] = email
            s.send_message(msg)
            s.quit()
            return redirect(url_for('reset'))
        return render_template("forget.html", msg ='There isn`t an username with this email.')
    return render_template("forget.html")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if session.get('loggedin') == True:
        return redirect(url_for('welkom'))
    if request.method == 'POST' and 'username' in request.form and 'code' in request.form and 'password' in request.form:
        username = request.form['username']
        code = request.form['code']
        password = request.form['password']
        cursor.execute('SELECT username FROM Speler WHERE username = %s AND code = %s', (username, code))
        result = cursor.fetchone()
        if result:
            source = string.ascii_letters + string.digits
            code = ''.join((random.choice(source) for i in range(8)))
            update = cursor.execute('update Speler set password = %s, code = %s where username = %s;', (password, code, username))
            conn.commit()
            return redirect(url_for('login'))
        return render_template("reset.html", msg='incorrect username and code combination')
    return render_template("reset.html")

@app.route('/welkom')
def welkom():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if 'loggedin' in session:
        account = display[0]
        return render_template('home.html', account=account)
    return redirect(url_for('login'))

@app.route('/challenges')
def challenges():
    if session.get('challenge1') == True:
        return redirect(url_for('challenge1'))
    if session.get('loggedin') == True:
        return render_template('challenges.html', button = 'logout', txt = 'Log out')
    return render_template('challenges.html', button = 'login', txt = 'Login')

@app.route('/start_challenge1')
def start1():
    if session.get('challenge1') == True:
        return render_template('challenge1.html')
    if session.get('loggedin') == True:
        return render_template('start1.html',start='challenge1' ,button = 'logout', txt = 'Log out' )
    return render_template('start1.html', start='#', button = 'login', txt = 'Login',  msg='U most be logged in before you can start a challenge' )

@app.route('/challenge1')
def challenge1():
    if session.get('challenge1') == True:
       return render_template('challenge1.html')
    if session.get('loggedin') == True:
       session['challenge1'] = True
       return render_template('challenge1.html')
    return redirect(url_for('challenges'))

@app.route('/admin')
def admin():
    if session.get('challenge1') == True:
       session.pop('challenge1', None)
       return render_template('admin.html')
    return redirect(url_for('challenge1'))

@app.route('/scoreboard')
def scoreboard():
    cursor.execute("SELECT `Speler`.`username`, `Score`.`score_challenge1`, `Score`.`score_challenge2`, `Score`.`score_challenge3`  FROM `pad`.`Score` INNER JOIN `pad`.`Speler` ON `Score`.`spelerscore_id` = `Speler`.`speler_id`;")
    data =cursor.fetchall()

    return render_template("scoreboard.html", score = data)
