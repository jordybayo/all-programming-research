# Random Forest on Iris Dataset
data("iris")
str(iris)

#step 1: split data in train and test
split <- sample.split(iris, SplitRatio = 0.7)
split


training_set = subset(iris, split == "TRUE")
test_set <- subset(iris, split == "FALSE")

#step 2: fitting Random Forest Classification to the training set
#install.packages('randomForest')
library(randomForest)
set.seed(123)

?randomForest
classifier = randomForest(x = training_set[-5],
                          y = training_set$Species,
                          ntree = 500)

#Step3: predict the test results
y_pred = predict(classifier, newdata = test_set[-5])

#making the confusion matrix
cm = table(test_set[, 5], y_pred)
cm


#step4: model evaluation
plot(classifier)
importance(classifier)
varImpPlot(classifier)
