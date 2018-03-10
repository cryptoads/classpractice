def hist(word):

    dict1 = {}
    for x in word:
        if dict1.get(x):
            dict1[x] += 1
        else:
            dict1[x] = 1
    print dict1


hist("banana")
