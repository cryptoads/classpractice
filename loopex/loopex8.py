count = 1
x = int(raw_input("Height of triangle?"))
for n in range(0, x):
    print (" " * (x - 1)) + "*" * count
    x -= 1
    count += 2
