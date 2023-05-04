#######################dates


today = Sys.Date()
today
class(today)

#creating date from
chr = "2019-12-04"
class(chr)

#convert
h = as.Date(chr)
class(h)

as.Date("2018/01/03")

dt = as.Date("September 18, 2008", format="%B %d, %Y")
weekdays(dt)
months(dt)
