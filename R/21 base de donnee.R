#importing Connection file and libraries

library(RMySQL)
source("Connector.R")

#creating connection to database
con <- ConnectDB("techcodefacil", "localhost", "root")

#creating querry
query <- dbSendQuery(conn, "SELECT * FROM unknowedDB")

#fetching data
data <- fetch(query, n = -1)

#disconnecting database connection
dbDiscconnect(con)

#manipulating Data
dataval <- na.omit(data) #omit not available data
print(dataval)

#dataval <- as.integer(dataval$column1, m=-1) #making value of first column integer

