
#inport scv
tsla <- read.csv(file.choose())
tsla1 <- read.csv("tsla.csv")
tsla1
class(tsla1)
str(tsla1)
intall.packages('readr')
library(readr)
gsl = read_csv('tsla.csv')

#import text
hd = read.table("hotdog.txt", sep = "\t", header = T)
hd

#from excel
install.packages('readxl')
library(readxl)
excel_sheets("tsla.xlsx")


##############export file

#file.txt
write.table(hd, file = "hum.txt", sep = "\t")

#file.xlsx
install.packages("writexl")
library(writexl)
write_xlsx(hd, "exp2.xlsx")

#wrirte csv
