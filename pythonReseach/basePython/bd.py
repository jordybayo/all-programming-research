#coding:utf-8

import mysql.connector

mydb = mysql.connect(
    host="localhost"
    user="root"
    passwd=""

)

print(mydb)