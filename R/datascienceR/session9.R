######################importing text files###########
sp <-  read.csv2("shopp.csv", header = TRUE, sep = ",")
View(sp)


# Naive bayes

#importing the dataset
dataset <- read.csv("Social_Network_Ads.csv") 
dataset = dataset[3:5]

# Encoding the target feature as a factor 
dataset$Purchased = factor(dataset$Purchased, levels = c(0, 1))

# splitting the dataset into a training set and Test set
# install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# feature scaling
training_set[-3] = scale(training_set[-3])
test_set[-3] = scale(test_set[-3])

# Fitting SVM to the training set
# install.packages("e1071")
library(e1071)
classifier = naiveBayes(x = training_set[-3],
                        y = training_set$Purchased)

# Predict the Test set result
y_pred = predict(classifier, newdata = test_set[-3])

# making the confusion matrix
cm = table(test_set[,3], y_pred)
cm

# evaluating the model
library(caret)
confusionMatrix(cm)

# visualizing the training set result ~ use it as a template
library(ElemStatLearn)
set = training_set
x1 = seq(min(set[,1])-1, max(set[,1]) + 1, by = 0.01)
x2 = seq(min(set[,2])-1, max(set[,2]) + 1, by = 0.01)
grid_set = expand.grid(x1, x2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set)
plot(set[,3],
     main = 'Native bayes (Training set)',
     xlab = 'Age', ylab = 'EstimatedSalary',
     xlim = range(x1), ylim = range(x2))
contour(x1,x2, matrix(as.numeric(y_grid), length(x1), length(x2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(grid_set, pch = 21, bg = ifelse(set[,3] == 1, 'green4', 'red3'))


# visualizing the test set results
library(ElemStatLearn)
set = test_set
x1 = seq(min(set[,1])-1, max(set[,1]) + 1, by = 0.01)
x2 = seq(min(set[,2])-1, max(set[,2]) + 1, by = 0.01)
grid_set = expand.grid(x1, x2)
colnames(grid_set) = c('Age', 'EstimatedSalary')
y_grid = predict(classifier, newdata = grid_set)
plot(set[,3],
     main = 'Native bayes (test set)',
     xlab = 'Age', ylab = 'EstimatedSalary',
     xlim = range(x1), ylim = range(x2))
contour(x1,x2, matrix(as.numeric(y_grid), length(x1), length(x2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(grid_set, pch = 21, bg = ifelse(set[,3] == 1, 'green4', 'red3'))


