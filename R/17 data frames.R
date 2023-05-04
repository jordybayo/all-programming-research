#data frames

#table structure to store data

employee.data <- data.frame(
  employee_id = c(1:4),
  employee_name = c("raj", "amit", "sahill", "rahit"),
  salary = c(11698, 356, 548778, 4578),
  stringsAsFactors = FALSE
  )

print(employee.data)

#get structure of data

str(employee.data)
summary(employee.data)

 
