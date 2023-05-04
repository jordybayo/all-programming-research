  #bar plot

count <- table(mtcars$gear)

print(count)

barplot(count, main="car Distribution", xlab="Number of gear")