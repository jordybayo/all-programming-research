############################DECISION TREE#################
#Exaple 1: mtcars
#decision tree
data(mtcars)
str(mtcars)
mtcars$vs <- as.factor(mtcars$vs)
mtcars$am <- as.factor(mtcars$am)

#using rpart function of rpart package
#step 1: Split data in train and test data
library(caTools)
set.seed(123)

split<-sample.split(mtcars, SplitRatio = 0.8)
split

train <- subset(mtcars, split == "TRUE")
test  <- subset(mtcars, split == "FALSE")
str(train)
str(test)


#step 2: Train model using rpart function of rpart package
#install.package("rpart")
library("rpart") ## recursive partitionnning
DecTreeModel <- rpart(am~. , data = train, method = "class")

#see the decision tree
#install("rpart.plot")
library("rpart.plot")
rpart.plot(DecTreeModel)

#Step 3: predict on test data
fitted.value <- predict(DecTreeModel, newdata = test, type = "class")
fitted.value

#step 4: Evaluate the model accuracy
table(test$am, fitted.value)
misClassError <- mean(fitted.value != test$am)
print(paste('accuracy = ', 1-misClassError))



###################################################################################################
#example More than two level
###################################################################################################
#decision tree IRIS

library(rpart)
library(rpart.plot)
library(e1071)

head(iris)
iris
decision_tree_model <- rpart(Species ~. , data = iris, method = "class")
decision_tree_model
rpart.plot(decision_tree_model)

# running rthe model in test and train
library(caTools)
set.seed(123)

split <- sample.split(iris, SplitRatio = 0.7)
split

train = subset(iris, split = "TRUE")
test <- subset(iris, split == "FALSE")
train
test

#train the model on train data
decision_tree_model = rpart(Species ~., data = train, method = "class")
summary(decision_tree_model)

#the summary show the statistics of all split

#The princp plotcp functions provide the cross-validation error for each nsplit
#the one with leat crossvalidated error (xerror) is optimal value of cpgiven
#minimum error occur when CP = 0.01
printcp(decision_tree_model)
?printcp

#minimum error occurs the tree size is = 3
plotcp(decision_tree_model)
?plotcp

#peailed information about the each node
summary(decision_tree_model)

###################################################################################################
#Example 3: chunrn data
###################################################################################################
#import churm data
churn_data = read.csv(file.choose())

str(churn_data)
#step 1: split data ain train and test data
library(caTools)
set.seed(350)
split<-sample.split(churn_data, SplitRatio = 0.7)
split

train <- subset(churn_data, split == "TRUE")
test <- subset(churn_data, split=="FALSE")
str(train)
str(test)

#step2 : Train model logistics regression using glm function
decision_tree_model2 = rpart(n_cores~ ., data = train, method = "class") 
decision_tree_model2 

summary(decision_tree_model2)
printcp(decision_tree_model2)
plotcp(decision_tree_model2)

rpart.plot(decision_tree_model2)

#predict test data based on trained model
test$n_cores_predicted = predict(decision_tree_model2, newdata = test, type = "class")

#Step4 : Evaluate model accuracy using confusion matrix
table(test$n_cores, test$n_cores_predicted)
library(caret)
confusionMatrix(table(test$n_cores, test$n_cores_predicted))

#tree Prunning
#find the value of CP for which cross validation is minute
min(decision_tree_model2$cptable[, "xerror"])
which.min(decision_tree_model2$cptable[,"xerror"])
cpmin <- decision_tree_model2$cptable[2, "CP"]

#prune the tree by setting the cp parameter as = cpmin
decision_tree_pruned = prune(decision_tree_model2, cp = cpmin)
rpart.plot(decision_tree_pruned)
printcp(decision_tree_pruned)
plotcp(decision_tree_pruned)
plotcp(decision_tree_pruned)

#predict test data based on trained model
test$n_cores_predicted = predict(decision_tree_pruned, newdata = test, type = "class")


# Evaluate Model accuracy confusion matrix
table(test$n_cores)
library(caret)
confusionMatrix(table(test$n_cores, test$n_cores_predicted))
