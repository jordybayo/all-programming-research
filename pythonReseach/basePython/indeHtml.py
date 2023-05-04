#coding:utf-8

import cgi
import http.cookies
import datetime
import os
import sys
import codecs

sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())


expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")

my_cookie=http.cookies.SimpleCookie()
my_cookie["pref_lang"]="fr"
my_cookie["pref_lang"]["expires"]=expiration 
my_cookie["pref_lang"]["httponly"]=True


print(my_cookie.output()) 
print("cont-type: text/html; charset=utf-8\n")

html="""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>page py en html</title>
</head>
<body>
    <h1>cookies avec python</h1>
"""
print(html)

try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("la langue choisi par l'utilisateur est: ", user_lang["pref_lang"].value)
except(http.cookies.CookieError, KeyError):
    print("Non trouvé")




html="""<p>il était une fois..</p>
<body>
</html>
"""

print(html)