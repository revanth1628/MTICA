def squares(x=0):
    while x<10:
        x=x+1
        yield x*x

##yieldeList=[i for i in squares()]
##print(yieldeList)

## materialise list from generator using list()
yieldeList =list(squares())
print(yieldeList)
