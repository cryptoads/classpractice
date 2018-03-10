import random


def inputNumber(message):
    while True:
        try:
            userInput = int(raw_input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return userInput
            break


def squaremake():
    square = inputNumber("What size square you want my man?")
    for n in range(0, square):
        print "*" * square


def trianglemake():
    count = 1
    x = inputNumber("Height of triangle?")
    for n in range(0, x):
        print (" " * (x - 1)) + "*" * count
        x -= 1
        count += 2


def boxmake():
    width = inputNumber("Width?")
    height = inputNumber("Height?")
    for x in range(0, height):
        if x == 0:
            print "*" * width
        elif x == height - 1:
            print "*" * width
        else:
            print "*" + (" " * (width - 2)) + "*"


def randomresponse():
    rand = random.randint(0, 5)
    if rand == 1:
        return "Look guy, I don't have time for this "
    elif rand == 2:
        return "Unlike your mom..."
    elif rand == 3:
        return "You dumb. "
    else:
        return "Why you so dumb? "


def playing():
    playing = raw_input("Would you like to keep playing? (Y/N)").lower()
    goodans = ["y", "n"]
    while playing not in goodans:
        playing = raw_input(randomresponse() + "I only accept Y or N. Try again.").lower()
    if playing == "n":
        print "Bye"
    elif playing == "y":
        menu()


def menu():
    print "1 Triangle \n 2 Square \n 3 box"
    choice = inputNumber("Choose a shape!")
    while choice > 3 or choice <= 0:
        print "Choice must be 1, 2 or 3"
        choice = inputNumber("Choose a shape!")
    if choice == 1:
        trianglemake()
    elif choice == 2:
        squaremake()
    elif choice == 3:
        boxmake()
    playing()


menu()
