width = int(raw_input("Width?"))
height = int(raw_input("Height?"))
for x in range(0, height):
    if x == 0:
        print "*" * width
    elif x == height - 1:
        print "*" * width
    else:
        print "*" + (" " * (width - 2)) + "*"
