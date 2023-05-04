import smtplib
from smtplib import SMTPException

sender = 'riguellebayo@gmail.com'
receivers = ['jordiibayo@gmail.com']

message = """From: From Person <riguellebayo@gmail.com>
To: To Person <jordiibayo@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")