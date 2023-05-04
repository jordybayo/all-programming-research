#opening file in R

#support for hadling file(read, write JSON,CSV,XML,TEXT etc...)

data1 <- read.csv("tsla")
print(data1)

print(is.data.frame(data1))

print(ncol(data1))
print(nrow(data1))

print(max(data1$price))
maxDetails <- subset(data1, KM == max(KM))
print(maxDetails)

writte.csv(maxDetails, "output.csv")
newData <- read.csv("output,csv")
print(newData)

