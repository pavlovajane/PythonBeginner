
someList = '01234567789343'
myIter = iter(someList)
length = len(someList)

for i in range(0,length):
    next_iter = next(myIter)
    print(next_iter)