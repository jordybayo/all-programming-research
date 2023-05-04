#database

#create database

library(RMySQL)

connectDB <- function(dbName, hostname, userName){
  sqlConnection <- NULL
  result = tryCatch({
    sqlConnection <- dbConnect(MySQL(), dbname=dbName, hsot=hostname, user=userName, password=.rs.askForPassword("Enter Password: "))
  }
  
  warning = function(w){
    print("warning")
    suppressWarnings()
  }
  
  error = functon(e){
    print("Error"+e)
  }
  
  finally = {
    print("Connected.. successfully")
  })
  
  return (sqlConnection)
}





