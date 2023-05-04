#################data manipulation

#appy
m = matrix(c(1,3,4,5), 2,2)
m
apply(m, 2, sum)
apply(m, 1, mean)

#lapply
list1 = list(a=c(1:6), b=c(2:9), c=c(9:8))
lapply(list1 , FUN = sum)
unlist(lapply(list1 , FUN = sum))
sapply(list1, FUN = median)

#vapply
vapply(list1, FUN=range, FUN.VALUE = double(2))
vapply(list1, FUN=sum, FUN.VALUE = double(1))

 #tapply
age = c(22,334,565,678,89,89,08)
gender = c("ffd",)
gender = c("ffd","ffd","ffd","ffd","ff","ffd","ffd")
f <- factor(gender)
f
tapply(age, f, mean)
  
#load dataset
library(datasets)
data()
View(mtcars)
class(mtcars)
mtcars$wt
mtcars$cyl
f <- factor(mtcars$cyl)
tapply(mtcars$wt, f, mean)

#mapply
l <- list(rep(1,3), rep(2,2), rep(3,1))
l
mapply(rep, 1:3, 3:1)