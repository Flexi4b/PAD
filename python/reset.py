import smtplib

sender_email = "syscribe@gmail.com"
password = "Hacker420"
rec_email = "iliastakassa@hotmail.com"
message = """\
Subject: Reset your password

click on url to change password.\n \nurl here"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
