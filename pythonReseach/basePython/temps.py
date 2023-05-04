#coding:utf-8

import time

print(time.time())
print()
print(time.localtime())
print("")
print(time.localtime().tm_year)

print(time.strftime('%H:%M:%S'))

import datetime

date = datetime.date(2018,8,12)
print(date)
aujourdhui = datetime.date.today()
print(aujourdhui)