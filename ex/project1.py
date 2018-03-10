import random
secret_answer = random.randint(1, 10)
playagain = "Y"


def game():
    guess = 5
    answer = int(raw_input("Can you guess the number? "))
    if answer == secret_answer:
        print "You win"
    else:
        while answer != secret_answer:
            guess -= 1
            print "You have " + str(guess) + " guesses left."
            if guess == 0:
                print "game over"
                break
            if answer < secret_answer:
                answer = int(raw_input("Too low, try again. "))
            elif answer > secret_answer:
                answer = int(raw_input("Too high, try again "))
        if answer == secret_answer:
            print "You win!"


game()
while playagain == "Y":
    playagain = raw_input("Play again? Y/N ").upper()
    if playagain == "Y":
        game()
    else:
        print "Good Bye"
