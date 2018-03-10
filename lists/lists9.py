matrix1 = [[4, 5], [3, 4], [6, 7]]
matrix2 = [[3, 4], [0, 6], [4, 5]]
result2 = []
result = []
list3 = []
count = 0
for x in matrix1:
    for y in x:
        result.append(y)

for z in matrix2:
    for i in z:
        result2.append(i)

for num in result:
    list3.append(num + result2[count])
    count += 1
print list3
