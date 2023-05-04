

library(dplyr)
#install.packages('hflights')
library(hflights)


hflights = read.csv('/home/youngdevps/PycharmProjects/matplotlib/TSLA.csv')
head(hflights)
str(hflights)
summary(hflights)

#change to a table 
hflights = tbl_df(hflights)
class(hflights)

#glympse at hflights
dplyr::glimpse(hflights)
glimpse(hflights)

#select query
tbls <- select(hflights, Date, Open, Low, Close)
glimpse(tbls)
select(hflights, starts_with("Da"))
select(hflights, ends_with("e"))
select(hflights, Date, starts_with("v"), ends_with("n"))

#mutate
loss = mutate(hflights, Adj.Colse = Close - Open)
loss 

#filter
good_volume = filter(hflights, Volume>1000000)
View(good_volume)
glimpse(good_volume)

#arrange
arrange(hflights, Volume)
arrange(good_volume, desc(High))

#summarise
summarise(hflights, max_high=max(High), avg_vol=mean(Volume))
    