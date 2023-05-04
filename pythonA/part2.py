list1 = []
list2 = []

for i in range(1, 11):
    list1.append(4*i)


for i in range(1, 10):
    list2.append(list1[i]%5==0)

print(list1)
print(any(list2))