# loops : while, repeat, for

#for iterate against a number of value
x <- LETTERS[1:7]

for (i in x){
  print(i)
}


#while execute a state of statement while a value is true
values <- c("while loop")
count <- 5

while (count < 7){
  print(values)
  count = count + 1
}


#while repeat a statement until it finds an end statement
#it's like a do-while
x <- c("Hello world")
count <- 2

repeat {
  print(x)
  count = count + 1
  
  if (count > 7){
    break()
  }
}


