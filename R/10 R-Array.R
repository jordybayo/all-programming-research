# arrays

#in R the start array index is 1 


#vector as input to the array
vector1 <- c(8,2,1)
verctor2 <- c(10,16,22,43,15,25)

result <- array(c(vector1,verctor2), dim = c(3,3,2))
print(result)

#accessing array elemetns
print(result[1,1,1])

result[3,3,1] -> mat1
result[2,2,1] -> mat2

print(mat1)
print(mat2)
print(mat1+mat2)
 