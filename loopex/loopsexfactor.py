factor = int(raw_input("Number to get factors from. "))


def factsolve(num):
    for x in range(1, num + 1):
        if (num % x == 0):
            print x


factsolve(factor)
