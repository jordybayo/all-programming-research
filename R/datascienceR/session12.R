####################solution for titanic Survived##############################

##############################################################################
# TItanic Survival Tutoraial - part 1 : creating First Prediction model
##############################################################################
# Titanic Dataset
#Import the Training and Test dataset
#train<-read.csv(file.choose(), stringsAsFactors = F, na.strings = c("", "NA", ""))
titanic_dataset<-read.csv(file.choose(), stringsAsFactors = F, na.strings = c("", "NA", ""))

#split the train and test set
split  <- sample.split(titanic_dataset, SplitRatio = 0.36)
train <- subset(titanic_dataset, split == "FALSE")
test <- subset(titanic_dataset, split == "TRUE")
str(train)
str(test)
summary(train)
summary(test)

##############################################################################
# Lazy Predictor
##############################################################################
#initialized a survived column to 0
test$Survived = 0
my_solution <- data.frame(PassergerId = test$PassengerId, Survived = test$Survived)

#check the row number - It should match with the test row number - 418
nrow(my_solution)

#writte  tthe soltion for submission
write.csv(my_solution, file = "Lazy_predictor.csv", row.names = FALSE)


##############################################################################
# First Predictor with Gender
##############################################################################
table(train$Sex, train$Survived)
prop.table(table(train$Sex, train$Survived))
#copy os test
test_one = test
#nitiakized a surviced column to 0
test_one$Survived <- 0
#set survived to 1 if sex == "female"
test_one$Survived[test$Sex == "female"] <- 1
my_solution <- data.frame(PassengerId = test$PassengerId, Survived = test_one$Survived)
#check the row number - It shoulf match with test row number - 418
nrow(my_solution)
#writte  tthe soltion for submission
write.csv(my_solution, file = "Gender_model.csv", row.names = FALSE)

##############################################################################
# Titanic survival Tutorial - part2 : data cleaning and preparation
##############################################################################
#combine train adn test datafor Dat cleaning and preparation
Full <- rbind(train, test)
View(Full)

#structure of the full data
str(Full)
summary(Full)

# Survival rates in absolutes numbers
table(Full$Survived)

#survival rates in proportions
prop.table(table(Full$Survived))

#Data type conversion
Full$Pclass = as.factor(Full$Pclass)

########################################################################################
#get percentage of missing value of the attributes - Appoach 2 )functionn)
sapply(Full, function(df){
  sum(is.na(df)==T)/length(df)
})
#Approach amelia package
library(Amelia)
missmap(Full, main = "Missing Map")

########################################################################################
########################################################################################
# Inputating Missing Value

# Missing Value Inputation - Age
Full$Age[is.na(Full$Age)] <- mean(Full$Age, na.rm = T)
sum(is.na(Full$Age))

# Missing Value Inputation - Class
Full$Class[is.na(Full$Class)] <- mean(Full$Class, na.rm = T)
sum(is.na(Full$Class))

# Missing Value Inputation - Body
table(Full$Body, useNA = "always")

# Missing Value Inputation - LifeBoat
table(Full$Lifeboat, useNA = "always")

# Missing Value Inputation - Destination
table(Full$Destination, useNA = "always")

# Missing Value Inputation - Boarded
table(Full$Boarded, useNA = "always")

# Missing Value Inputation - Hometown
table(Full$Hometown, useNA = "always")

# Missing Value Inputation - AgeWiki
Full$Age_wiki[is.na(Full$Age_wiki)] <- mean(Full$Age_wiki, na.rm = T)
sum(is.na(Full$Age_wiki))

# Missing Value Inputation - NaameWiki
table(Full$Name_wiki, useNA = "always")

# Missing Value Inputation - WikiId
Full$WikiId[is.na(Full$WikiId)] <- mean(Full$WikiId, na.rm = T)
sum(is.na(Full$WikiId))

# Missing Value Inputation - Embarked
table(Full$Embarked, useNA = "always")
#substitute the missing values with the mode value
Full$Embarked[is.na(Full$Embarked)] <- 'S'
sum(is.na(Full$Embarked))
table(Full$Embarked, useNA = "always")

# Missing Value Inputation - Survvived
table(Full$Survived, useNA = "always")
#substitute the missing values with the mode value
Full$Survived[is.na(Full$Survived)] <- '0'
sum(is.na(Full$Survived))
table(Full$Survived, useNA = "always")

#missing value imputing - Fare
# subsitute  the missing values  with the average value
Full$Fare[is.na(Full$Fare)] <- mean(Full$Fare, na.rm = T)
sum(is.na(Full$Fare))

#missing value imputing - Cabin
# subsitute  the missing values  with the average value
Full <- Full[-11]
Full <- Full[-18]
Full <- Full[-17]
Full <- Full[-16]
Full <- Full[-15]
Full <- Full[-14]
Full <- Full[-13]
Full <- Full[-12]

# check again for NA
sapply(Full, function(df){
  sum(is.na(df)==T)/length(df)
})


# Data cleaning is done , now we will again split back the data into train and test
# Train test splitting - why do we need it?
train_cleaned <- Full[1:891,]
test_cleaned <- Full[892:1309,]

##############################################################################
# Titanic survival Tutorial - part3 : data exploration
##############################################################################


##############################################################################
# Future Engeeneering
##############################################################################
#Engineering variable1 : child
# Engineering variable 2: Title
# Engeening variable 3: Familly size
##############################################################################

#Engeineering variable 1 : child
# create the column child, and indicate wether child or no child
Full$Child <- NA
Full$Child[Full$Age<18] <- 1
Full$Child[Full$Age >= 18] <- 0
str(Full$Child)
ggplot(Full) + geom_bar(aes(x=Child))

#Engineering variable 2 : Title
# Extract the title - Mr , Mrs, Miss
Full$Title <- sapply(Full$Name, FUN = function(x){strsplit(x, split = '[,.]')[[1]][2]})
Full$Title <- sub('', '', Full$Title) #remove thwhite space blank
table(Full$Title)
ggplot(Full) + geom_bar(aes(Full$Title))


# Combine small title groups
#Full$Title[Full$Title %in% c('Mme', 'Mlle')] <- 'Mlle'
#Full$Title[Full$Title %in% c('Capt', 'Don', 'Major', 'Sir', 'Master', 'Dr', 'Rev')] <- 'Sir'
#Full$Title[Full$Title %in% c('Dona', 'Lady', 'the Countess', 'Jonkheer')] <- 'Lady'

levels(Full$Title) <- sub("Mme", "Mlle", levels(Full$Title))
levels(Full$Title) <- sub("Mlle", "Mlle", levels(Full$Title))
levels(Full$Title) <- sub("Miss", "Mlle", levels(Full$Title))

levels(Full$Title) <- sub("Capt", "Sir", levels(Full$Title))
levels(Full$Title) <- sub("Don", "Sir", levels(Full$Title))
levels(Full$Title) <- sub("Major", "Sir", levels(Full$Title))
levels(Full$Title) <- sub("Sir", "Sir", levels(Full$Title))
levels(Full$Title) <- sub("Master", "Sir", levels(Full$Title))
levels(Full$Title) <- sub("Dr", "Sir", levels(Full$Title))
levels(Full$Title) <- sub("Rev", "Sir", levels(Full$Title))

levels(Full$Title) <- sub("Dona", "Lady", levels(Full$Title))
levels(Full$Title) <- sub("Lady", "Lady", levels(Full$Title))
levels(Full$Title) <- sub("the Countess", "Lady", levels(Full$Title))
levels(Full$Title) <- sub("Jonkheer", "Lady", levels(Full$Title))
#convert to factor
Full$Title <- factor(Full$Title)
table(Full$Title)
ggplot(Full) + geom_bar(aes(x=Title))

# Engineer variable 3: familly size
Full$FamillySize <- Full$SibSp + Full$Parch + 1
table(Full$FamillySize)
ggplot(Full) + geom_bar(aes(x=FamillySize))

# Split back into test and train sets
train_featured <- Full[1:891,]
test_featured <- Full[892:1309,]

train_featured$Survived = as.factor(train_featured$Survived)
train_featured$Sex = as.factor(train_featured$Sex)
train_featured$Embarked = as.factor(train_featured$Embarked)

test_featured$Sex = as.factor(test_featured$Sex)
test_featured$Embarked = as.factor(test_featured$Embarked)

##############################################################################
# Titanic Survival Tutorial - part5 : Logistic Regression
##############################################################################
##############################################################################
# Step 1 : Split data in train and test data
#install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(train_featured, SplitRatio = 0.8)
split

train.data = subset(train_featured, split == "TRUE")
test.data = subset(train_featured, split == "FALSE")

str(train.data)
str(test.data)

##############################################################################
# Step 2 : Train the model with Logistic regression using glm function

# Model fitting - try 1 : without feature Engineering
# After removing Passenger ID, Name and ticket
logit_model1 = glm(Survived ~., family = binomial(link = 'logit'), data = train.data[-c(1,4,9,13,14,15)])
summary(logit_model1) # AIC : 650.2

# Model fitting - try 2 : with feature Engineering
# After removing Passenger ID, Name and ticket , child, Title, Family size
logit_model2 = glm(Survived ~., family = binomial(link = 'logit'), data = train.data[-c(1,4,14,9)])
summary(logit_model2) # AIC : 630.44 more lesser tha model 1

anova(logit_model1, logit_model2, test = 'Chisq')

anova(logit_model2, test = 'Chisq')  

##############################################################################
# Step 3 : Predict test data based on trained model - logit_model
fitted.results = predict(logit_model2, newdata = test.data, type = 'response')

##############################################################################
#Step 4 : Change probabilities to class (0 or 1/yes or No)
# If prob > 0.5 then 1, else 0 . Threshold can be set better results
fitted.results <- ifelse(fitted.results > 0.5, 1, 0)

##############################################################################
library(caret)
confusionMatrix(table(test.data$Survived, fitted.results))

#ROC- AUC plot
install.packages("ROCR")
library(ROCR)
ROCPred <- prediction(fitted.results, test.data$Survived)
ROCPerf <- performance(ROCPred, measure = 'tpr', x.measure = 'fpr')

par(mfrow = c(1,1))
plot(ROCPerf, colorize = TRUE, print.cutoffs.at = seq(0.1, by = 0.1), main="ROC CURVE")
abline(a=0, b=1)

auc <- performance(ROCPred, measure = "auc")
auc <- auc@y.values[[1]]
auc <- round(auc, 4)
legend(.0, .4, auc, title = "AUC", cex = 1)

##############################################################################
# Make predictions on the test set
my_prediction = predict(logit_model2, test_featured, type = "response")

# If prob > 0.5 then 1, else 0 . Threshold can be set better results
my_prediction = ifelse(my_prediction>0.5,1,0)
#Finish the dataset.frame() call
my_solution = data.frame(PassengerId = test_featured$PassengerId, Survived = my_prediction)
# Use nrow on my_solution should be 418
nrow(my_solution)

# Finish the writte .csv() call
write.csv(my_solution, file = "my_solution_logit.csv", row.names = FALSE)
############################################################################## 
logit_model3 = glm(Survived~., family = binomial(link = 'logit'), data = train_featured[-c(1,4,9)])
summary(logit_model3)

my_prediction = predict(logit_model3, test_featured, type = 'response')

my_prediction = ifelse(my_prediction > 0.5,1,0)

my_solution = data.frame(PassengerId = test_featured$PassengerId, Survived = my_prediction)

nrow(my_solution)
write.csv(my_solution, file = "my_solution_logit2.csv", row.names = FALSE)
