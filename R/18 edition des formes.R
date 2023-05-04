#reshaping(row cobine, column combine)

#chaging how data is represented in rows and columns

#create vertors objects
city <- c("yaounde", "douala", "bamenda", "bafoussam", "limbe", "bertoua")
zipcode <- c(305988, 879954,    336987,    142324,      698989)

#combines above vectors into one data frame
oldAddressess <- cbind(city, zipcode)
print(oldAddressess)

newAddresses <- data.frame(
  city = c("limbe", "buea"),
  zipcode = c("879899", "879991")
)
print(newAddresses)

#combines rows from both of data frames
totalAdresses <- rbind(oldAddressess, newAddresses)
print(totalAdresses)


