#list

# can have any long of value from different types
#notice/remember index in R begin with one(1) 

#create
list_data <- list("red", c(1,2,3), TRUE, 56.14, 2+3i)
print(list_data)

#access
print(list_data[1])
print(list_data[3])

#ADD elements
list_data[7] <- "new elemeemt"
print(list_data)

#Remove
list_data[7] <- NULL
print(list_data)

#update 
list_data[1] <- "black"
print(list_data)

