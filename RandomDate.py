import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    rng = random.random()
    dateFormat = "%m/%d/%Y"
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + rng * (endTime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

print("Random date =", getRandomDate("1/1/2020", "1/1/2026"))