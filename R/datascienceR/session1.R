library('ggplot2')
library('ggthemes')
library('scales')
library('dplyr')
library('mice')
library('randomForest')
library('caret')


########help functions############
?mean
help(mean)

#example of function use
example(mean)
example(sd)

sd(c(1:10), na.rm = FALSE)
sqrt(0)
ceiling(3.00001)
floor(5.9)
exp(2)
log(10)

x =(1:5)
x = append(x, 6)
x
length(x)
identical(7,7)
range(x)
rep(x, 3)
rev(1:3)
seq(5,100,5)
unique(c(1,2,3,1,5,2))

#statistical functions
mean(1:3)
median(1:3)
sd(1:3)
min(1:3)
max(3:1)
range(1:3)

#character functions
x <- "abcdefghij"
substr(x, 2,3)
grep(pattern = 'bcd', x=x, ignore.case = TRUE)
sub(pattern = 'b', x=x, replacement = 'B', ignore.case = T) #replace at the first
gsub(pattern = 'b', x=x, replacement = 'B', ignore.case = T) #replace at all
paste(x, 'klmn')

#writtings functions
math_magic <- function(a,b=1){
  a*b * a/b
}
math_magic(2)
