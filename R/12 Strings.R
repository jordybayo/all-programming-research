# les chaines de caracteres

#any value names with one or two quotes is knowned as a string

a <- "valid ' string"
print(a)

b <- 'valid " string' 
print(b)

c <- 'Mixed quotes invalid'
print(c)

#f <- 'single quote ' inside single quote'
print(f)

#manipulation
abc = "l'apprentissage"
def = "va vite avec"
hij = "le TechCoDeFacil"

print(paste(abc,def,hij))
print(paste(abc,def,hij, sep="~"))
print(paste(abc,def,hij, sep="", collapse=""))