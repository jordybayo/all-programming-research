#coding:utf-8


import time
import datetime as dt



print(time.time())
print(dt.MINYEAR)
print(dt.date)
print(dt.time.hour)
d = dt.timedelta(days = 1 , hours=48)
print("seconde:{}".format(d.seconds ))
print(dt.date.today())
print(dt.date.month)
print(dt.date(2018,10,18).weekday()) #return the isoweek day
print(dt.date(2018,10,18).isoweekday()) #the day of the week
print(dt.date(2018,10,18).isocalendar()) #return a tuple(iso year, iso week,iso days )
print(time.ctime())
print(time.ctime())
print(dt.date.strftime(format))