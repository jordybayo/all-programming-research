#matrix

#object in which elements are store in 2D rectangular shape
#create
m1 <- matrix(c(3:14), nrow=4, byrow=TRUE)
print(m1)

#access
print(m1[1,3])


Q <- matrix(c(14:25), nrow=4, byrow = TRUE)
print(Q)

print(m1 + Q)
print(m1 * Q)
print(Q / m1)
print(m1 - Q)
