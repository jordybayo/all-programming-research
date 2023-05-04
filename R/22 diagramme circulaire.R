#pie charts

slices <- c(90, 12, 5, 13, 36)
lbs <- c("work", "sport", "familly", "games", "read")
pie(slices, labels = lbs, main="Activities Time")

# 3D pie chart
install.packages(plotrix)
library(plotrix)

slices <- c(90, 12, 5, 13, 36)
lbs <- c("work", "sport", "familly", "games", "read")
pie3D(slices, labels=lbls,explode=0.1,main="Activities in 3D")

