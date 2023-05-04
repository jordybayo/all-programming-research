#coding:utf-8


import re

#expression reguliaire pour recuperer  le numero de telephone
chaine = " ";
expression = r"^0[0-9] ([ .-]?[0-9]{2}){4}$"
while re.search(expression,chaine) is None:
	chaine =input("entrer votre numero de phone : ")



#expresion reguliaire pour recuperer l'addresse mail
chaine2 = str();
expression2 = r"^[A-Za-z0-9]{1,}[@]{1,1}[A-Za-z0-9]{1,40}[.]{1,1}[A-Za-z0-9]{1,5}$"
while re.search(expression2,chaine2) is None:
	chaine2 = input('entre ton addresse : ')


#code pour envoyer un mail

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'XXX@gmail.com'
msg['To'] = 'YYY@gmail.com'
msg['Subject'] = 'Le sujet de mon mail'
message = 'bonjour !'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.gmail.com', 587)
mailserver.ehlo()
mailserver.login('XXX@gmail.com','PASSWORD')
mailserver.sendmail('XXX@gamil.com','XXX@gmail.com',msg.as_string())
mailserver.quit()


unechaine = "abcdef"
print(unechaine)
unechaine = unechaine.replace("ab", "fuck")
print(unechaine)



#remplacement de caractere 'ab' par ' ab '
expression3 = r"^(a)b(cd)$"
remplace = re.sub(r"ab" , r" \1 ", "abcdef")


#compilation des expressions reguliaire
mot_passe = str()
exp_condition = r"^[A-Za-z0-9]{6,}$"
exp_exe = re.compile(exp_condition)
while exp_exe.search(mot_passe) is None:
	mot_passe = input("Mot de passe : ")
