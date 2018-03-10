def wordhisto(para):
    hist = {}
    for x in para.split():
        if hist.get(x):
            hist[x] += 1
        else:
            hist[x] = 1
    hist = sorted(hist, key=hist.get)[::-1]
    print hist[0:3]


wordhisto('this this this this that that that am am i  though you ok a')
