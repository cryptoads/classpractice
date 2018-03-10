list1 = (1, 2, 3)
list2 = (4, 5, 6)
count = 0
list3 = []
for num in list1:
    list3.append(num * list2[count])
    count += 1
print list3
