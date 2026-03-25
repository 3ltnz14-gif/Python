def SqValues(beg, end):
    lst = []
    for i in range(beg, end):
        lst.append(i**2)
        lsteven = []
        lstodd = []

    for i in lst:
        if i %2 == 0:
            lsteven.append(i)
        else:
            lstodd.append(i)

    print("Here's a list of even squares within specified range:", lsteven)
    print("Here's a list of odd squares within specified range:", lstodd)

beg = int(input("Enter starting number: "))
end = int(input("Enter end number: "))
SqValues(beg, end)