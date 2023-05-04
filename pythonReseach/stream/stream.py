def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()

print(next(gen))
print(next(gen))


print(next(gen), "good")
# for i in infinite_sequence():
#     print(i, end=" ")
