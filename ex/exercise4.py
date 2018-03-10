def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

this = inputNumber("Enter bill amount. ")
total = 0
that = 0
tipAmnt = 0
splitDatBillMyGuy = ""

def totalFunc(x):
	total =(int(this)*x) + int(this)
	print("Your tip total is "+ str(int(this)*x))
	splitDatBillMyGuy = inputNumber("How many people you trying to split this bill with, family? ")
	print("That's going to be "+str((total)/float(splitDatBillMyGuy))+" per person my guy!")

while tipAmnt == 0:
	that = input("Was the service good?")
	if that == "good":
		tipAmnt = .20
		totalFunc(tipAmnt)
	elif that == "fair":
		tipAmnt = .15
		totalFunc(tipAmnt)
	elif that == "bad":
		tipAmnt = .10
		totalFunc(tipAmnt)		
	else:
		print("Answer must be good, fair or bad")


