#web data

#fetch some data from the web

install.packages("RCurl")


library(RCurl)

sample <- read.table("http://ats.ucla.edu/stat/examples/arg/angell.txt")

print(sample)