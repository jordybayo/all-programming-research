
#vector
v = c(1:30)
v = c(T, F)
v = c(TRUE, 1, 5, 5.2)
class(v)
v = c(TRUE, 1, 5, 5.2, 'ff')

#matrices
m = matrix(c(1:30), nrow = 5, ncol = 6, byrow = T)
m = matrix(c(1:30), nrow = 5, ncol = 6, byrow = F)
m
m[1,2]

#array
a = array(c(1:27), dim = c(3,3,3))
a
a[1,2,2]

#data frame
id = c(2,3,5)
name = c('ba', 'asds', 'asd')
admis = c(T, F, T)
df = data.frame(id, name, admis)
df

#inbuilt data frame
mtcars
head(mtcars)
tail(mtcars)
str(mtcars)
summary(mtcars)
mtcars[1:2, 1:3]
df$admis #column
df['id']
df[2,] #column
df[-c(2,3)]
cars1 =subset(mtcars, cyl>6)
cars1
d1 = df['id']
d2 = df['name']
dr1 = mtcars[1:20, ]
str(dr1)
dr2 = mtcars[21:30,]
str(dr2)
d2
df_full <- cbind(d1, d2)
df_full
dr_full <- rbind(dr1, dr2)
dr_full
mtcars$gear = as.factor(mtcars$gear)
str(mtcars)

#list
liste <- list(v, m, df)
liste
names(my_list) <- c("v", "mat", "df")
my_list
