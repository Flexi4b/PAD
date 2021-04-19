#!/usr/bin/env python


#!/usr/bin/env python3
from http import cookies
import urllib.parse, cgi, cgitb

#get parameters
params = cgi.FieldStorage()
name = params.getvalue("username")
password = params.getvalue("password")


#set cookies
#set expiration time in 1 hour
expires = 60*60

mycookie = cookies.SimpleCookie()
mycookie["Name"] = name
mycookie["Passsword"] = password
mycookie["Password"]['expires']= expires

print (mycookie) #BEFORE content-type line

print( "Content-type:text/html\n")

print (""“
<!DOCTYPE html>
<html>
<head>
<meta charset = "utf-8“>
<title>Storing cookies</title>
</head>
<body>
<h1>2 cookies were stored!</h1>
""“)
print ("<h2>Name: "+ name +
"<br /> Password: "+password + "</h2>")
print("</body></html>")




