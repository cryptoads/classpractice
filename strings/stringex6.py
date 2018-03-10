vow = ("aa", "ee", "ii", "oo", "uu")
word = raw_input("give me a word. ")
result = ''
for index in range(len(word)):
    twoletters = word[index:index + 2]
    if twoletters in vow:
        result += word[index] * 4
    else:
        result += word[index]

print result
