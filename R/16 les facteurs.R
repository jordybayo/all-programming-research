#R factors

#use to store data in differents levels

data <- c("East", "West", "East", "West", "West", "north")

#Apply factor
factor_data <- factor(data)
print(factor_data)

#generating factors labels
#3 is an integer giving the number of levels
#4 is an integer f=ginving the number of replications

  v <- gl(3,4, labels = c("abc" , "def", "asc"))
  print(v)