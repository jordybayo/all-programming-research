######################Data visualisation

#Boxplot
vec <- c(2,3,5,6,4,8,1,2,3,2,4,30,40)
?boxplot
boxplot(vec, varwidth = T)

mtcars
boxplot(mpg~cyl, data = mtcars)
boxplot(mpg~cyl, data = mtcars, main="car village data",
        xlab="Number of cylenders", ylab="Miles per Gallon", col=c("gold", "darkgreen", "blue"))

#mosaic plot
data(HairEyeColor)
mosaicplot(HairEyeColor)


#heatmap
install.packages("MASS")
library(MASS)
mtcars
heatmap(as.matrix(mtcars))
?heatmap
m = matrix(c(1:30), nrow = 5, ncol = 6, byrow = F)
m1 = as.matrix(mtcars)
class(m1)
m2 <- select(hflights, starts_with("g"), starts_with("v"), ends_with("n"))
heatmap(as.matrix(m2), Rowv = NA, Colv = NA,scale = "column", col = cm.colors(256), xlab = "Attributes", main = "heatmap")

#3D graphs
install.packages("lattice")
library(lattice)
attach(iris)
str(iris)
View(iris)
View(lattice)
?cloud
cloud(Sepal.Length~Sepal.Width*Petal.Length)
cloud(Sepal.Length~Sepal.Width*Petal.Length, main = "3D scatterplot")
cloud(hp~mpg*wt|am, data = mtcars, main = "3D scatterplot", col = mtcars$cyl, pch=17)

#Plotly
install.packages("plotly")
library(plotly)

plot_ly(mtcars, x=~wt, y=~hp, z=~qsec)

#3d scattter plot with color
mtcars$am[which(mtcars$am==0)]<-"Automatic"
mtcars$am[which(mtcars$am==1)]<-"Manual"
mtcars$am <- as.factor(mtcars$am)
View(mtcars)
??plot_ly
#3D plot with color
plot_ly(mtcars, x=~wt, y=~hp, z=~qsec, color =~am, colors = c("#8F382A", "#0C4B8E")) %>% 
        add_markers() %>% 
          layout(scene = list(xaxis = list(title = "Weight"),
                              yaxis = list(title = "horsepower"),
                              zaxis = list(title = "qsec")))

#3D plot with color scaling
plot_ly(mtcars, x=~wt, y=~hp, z=~qsec, 
        marker = list(color = ~mpg, colorscale = c("#FFE1A1", "#0C4B8E"))) %>% 
        add_markers() %>% 
        layout(scene = list(xaxis = list(title = "Weight"),
                            yaxis = list(title = "horsepower"),
                            zaxis = list(title = "qsec")),
                annotations = list(
                  x = 1.13,
                  y = 1.05,
                  text = 'Miles/(US) gallon',
                  xref = 'paper',
                  yref = 'paper',
                  showarrow = TRUE
                ))

library(plotly)

#volcano data
str(volcano)
View(volcano)

#the 3D surface map
plot_ly(z = ~volcano, type = "surface")

#Correlations
install.packages("corrplot")
library(corrplot)
#check if all the variables arew numeric
mtcars$am <- 0
View(mtcars)
#compute the correlation matrix of these variables
corrMat <- cor(volcano)
#Generate the correlation plot
corrplot(corrMat)
#Generate the correlation ellipse plot
corrplot(corrMat, method = "ellipse")

# Load packages
install.packages("wordcloud")
install.packages("RColorBrewer")

library(wordcloud)
library(RColorBrewer)

#create model_table of manufacturer frequences
rownames(mtcars)
model_table <- table(rownames(mtcars))
model_table
#create the default wordcloud from this table
#scale - range of the size of the cloud
#freq - frequence of word
wordcloud(words = names(model_table), 
          freq= as.numeric(model_table),
          scale = c( 1, 0.25))

#change the minimum word frequency
#min.freq - below min.freq word will not be plotted
wordcloud(words = names(model_table),
          freq = as.numeric(model_table),
          scale = c(1, 0.25),
          min.freq = 1)


####################graphics with ggplot2##############
library(ggplot2)
#1 Data layer
#2 Aesthic layer
#3 Geometric
#4 Facet layer
#5 statistic
#6 Coordinates layer
#7 Themes layer
 
#scatter plot
ggplot(mtcars, aes(x=wt, y = mpg)) #2 layer
ggplot(mtcars, aes(x=wt, y = mpg)) + geom_point() # 3 layer
ggplot(mtcars, aes(x=wt, y = mpg, col = disp)) + geom_point() # adding colors
ggplot(mtcars, aes(x=wt, y = mpg, col = factor(cyl))) + geom_point() # adding colors by factor or levels
ggplot(mtcars, aes(x=wt, y = mpg, size = disp)) + geom_point() # adding colors by size 
ggplot(mtcars, aes(x=wt, y = mpg, col = factor(cyl), shape = factor(am))) + geom_point() # adding colors by factor or levels
ggplot(mtcars, aes(x=wt, y = mpg, col = factor(cyl), shape = factor(am), size = disp)) + geom_point() # adding colors by factor or levels


#################################################
#bar plot
p <- ggplot(mtcars, aes(x = factor(cyl)))
p
p + geom_bar()
ggplot(mtcars, aes(x=factor(cyl), fill=factor(am))) + geom_bar()

#histograms
ggplot(mtcars, aes(x=mpg)) + geom_histogram()
ggplot(mtcars, aes(x=mpg)) + geom_histogram(binwidth = 5)
ggplot(mtcars, aes(x=mpg)) + geom_histogram(binwidth = 5, color = "black")
ggplot(mtcars, aes(x=mpg)) + geom_histogram(binwidth = 5, color = "blue")

#Density plot
ggplot(mtcars, aes(x=mpg)) + geom_density(color = "black", fill = "blue")

#boxplot
ggplot(mtcars, aes(x=factor(cyl), y=mpg)) + geom_boxplot(color = "black", fill = "blue")


###########Facet layer
#plit the whole dataset based on a character along eow and clumn
mtcar2 <- mtcars
View(mtcar2)
mtcar2$am[which(mtcar2$am == 0 )] <- "Automatic"
mtcar2$am[which(mtcar2$am == 1)] <- "Manual"
View(mtcar2)
mtcar2$am <- as.factor(mtcar2$am)

ggplot(mtcar2, aes(x=wt, y=mpg, shape=factor(cyl), col=qsec)) + 
        geom_point() + facet_grid(.~am) 
#basic scatter plot
p <- ggplot(mtcar2, aes(x=wt, y=mpg))+geom_point()
p 
#separate column according am
p + facet_grid(am~.) #by row
#separate according cyl
p + facet_grid(.~cyl)
#separate by both column and row
p + facet_grid(am ~ cyl)


######################Statistics layer
ggplot(mtcar2, aes(x=wt, y=mpg)) + geom_point() + stat_smooth(method = lm, col = "red")
ggplot(mtcar2, aes(x=wt, y=mpg)) + geom_point() + stat_smooth()
ggplot(mtcar2, aes(x=wt, y=mpg)) + geom_point() + stat_smooth(method = lm)
ggplot(mtcar2, aes(x=wt, y=mpg)) + geom_point() + stat_smooth(method = lm, se = FALSE)
ggplot(mtcar2, aes(x=wt, y=mpg, col = factor(cyl))) + geom_point() + stat_smooth(method = lm, se = FALSE)


######################coordinates layer
#coordinates plot dimensions

#zoom in
ggplot(mtcar2, aes(x=wt, y=mpg)) + 
        geom_point() + 
        stat_smooth(method = lm, col="red") +
        scale_y_continuous('mpg', limits = c(2,35), expand = c(0,0)) + 
        scale_x_continuous('wt', limits = c(0,20), expand = c(0,0)) + 
        coord_equal() #1:1 aspect ratio

p <- ggplot(mtcar2, aes(x=wt, y=hp, col=am)) + 
        geom_point() + 
        stat_smooth() 
p + coord_cartesian(xlim = c(3,6)) #zoom in
p + coord_cartesian(xlim = c(2,6)) #zoom out


######################Theme layer
#starting point
p <- ggplot(mtcar2, aes(x=wt, y=mpg)) + geom_point()
z = p + facet_grid(.~cyl)
z
#plot 1 : changing the plot backg fill to darkgrey
z + theme(plot.background = element_rect(fill = "darkgrey"))
#adjust the border to be a black line of size 3
z + theme(plot.background = element_rect(fill="darkgrey", color="black", size=3))
#recyckle themes
#save themes
#use of element
mtcar_theme = theme(panel.background = element_blank(),
                    plot.background = element_rect(fill = "lightyellow"),
                    legend.key = element_blank(),
                    strip.background = element_rect(color = "green"),
                    
                    axis.text = element_text(colour = "blue"),
                    axis.text.x = element_text(angle = 45),
                    strip.text = element_blank(),
                    
                   panel.grid.major = element_line(colour = "lightblue"),
                   panel.grid.minor = element_line(colour = "pink"),
                   axis.line = element_line(colour = "lightblue")
)
mtcar_theme
p
p + facet_grid(am~cyl)
#recycle thems
p + facet_grid(am~cyl) + mtcar_theme

#inbuilt themes
p + facet_grid(am~cyl) + theme_classic()
p + facet_grid(am~cyl) + theme_bw()
p + facet_grid(am~cyl) + theme_dark()
p + facet_grid(am~cyl) + theme_get()
p + facet_grid(am~cyl) + theme_gray()
p + facet_grid(am~cyl) + theme_light()
p + facet_grid(am~cyl) + theme_linedraw()
p + facet_grid(am~cyl) + theme_void()
p + facet_grid(am~cyl) + theme_update()
p + facet_grid(am~cyl) + theme_replace()
