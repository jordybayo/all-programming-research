

library(corrplot)
#check if all the variables arew numeric
str(mtcars)
#compute the correlation matrix of these variables
View(mtcars)
corrMat <- cor(mtcars)
#Generate the correlation plot
corrplot(corrMat)
#Generate the correlation ellipse plot
corrplot(corrMat, method = "ellipse")