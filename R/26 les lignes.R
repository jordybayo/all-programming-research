#line graphs

x <- c(1:3)
y <- x #same data

par(pch=19, col="red") #ploting symbol and color

par(mfrow=c(2,4))#all plot on one page

ops = c("p", "l", "o", "b", "c", "s", "S", "h")

for (i in 1:length(ops)) {
  heading = paste("type=",ops[i])
  plot(x,y,type = "n",main = heading)
  lines(x,y,type = ops[i])
}