leet = {"a":4, "e":3, "g":6, "i":1, "o":0, "s":5, "t":7 }
thing = raw_input("give me string ")
for x in thing.lower():
	for y in leet:
		if x == y:
			thing = thing.replace(x, str(leet[y]))
print thing