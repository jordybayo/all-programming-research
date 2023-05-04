######################importing text files###########
df <-  read.csv2("GOOG.csv", header = TRUE, sep = ",")
di <- iris
View(df)

###########################data exploration#################
dim(di)
nrow(di)
ncol(di)
str(di)
table(di$Species)
summary(di)
names(di)
colnames(di)
head(di, 10) #by default give 5 or 6

########################Identify missings values##############
#data type conversion
di$Species = as.factor(di$Species)
str(di)
#identifying missings values
summary(di)
table(is.na(di))
sapply(di, function(x) sum(is.na(x)))
#blanc count of all
table(di$Sepal.Length)
table(di$Petal.Width)
sapply(di, function(x) sum(x==""))

i1 = iris
head(i1)
View(i1)
summary(i1)
#detect na values - approach 1 (lenght)
is.na(i1$Sepal.Length)
is.na(i1$Sepal.Width)
is.na(i1$Petal.Length)
is.na(i1$Petal.Width)
is.na(i1$Species)
sum(is.na(i1$Sepal.Length))
sum(is.na(i1$Petal.Width)) #fast way to see number of na values
sum(is.na(i1$Sepal.Length)==TRUE)/length(i1$Sepal.Length) #get the percentage of missings value of the attribute
#get percenetage of missing value of the attributes - approach 2(function)
sapply(df, function(df){
  sum(is.na(df)==T)/length(df)
})

install.packages("amelia")
library(Amelia)
########################data cleaning | treat missings values##############
#input missing values

sum(is.na(i1$Sepal.Length)==TRUE)/length(i1$Sepal.Length)
train <-  read.csv2("train.csv", header = TRUE, sep = ",")
View(train)
sapply(train, function(train){
  sum(is.na(train)==T)/length(train)
})
sapply(train, function(x) sum(x==""))
sum(is.na(train$Age)==TRUE)/length(train$Age)

#substitute the missing value with the average value
train[is.na(train$Age)] <- mean(train$Age, na.rm = TRUE)
sum(is.na(train$Age))


# missing value Inputation - embarked charachter values
table(train$Embarked, useNA = "always") #mode = S
train$Embarked[is.na(train$Embarked)] <- 'S'

#missing value Inputation - Fare
#substitut the missing value with the average value
train$fFare[is.na(train$Fare)] <- mean(train$Fare, na.rm = T)
sum(is.na(train$Fare))
sapply(train, function(df){
  sum(is.na(df)==T)/length(df)
})
########################data exploration | Identify missings values##############

