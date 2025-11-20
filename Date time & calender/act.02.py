import random
import time

def getRandomDate(satarDate, endDate):
    print("Printing Random Dates between", satarDate, "and", endDate)
    randomGenerator = random.Random()
    dateFormat = "%m-%d-%Y"

    startTime = time.mktime(time.strptime(satarDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator.random() * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
print(getRandomDate("1-1-2020", "12-31-2023"))