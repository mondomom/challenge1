import sys
import numpy, math



def task1(*numList):
    out1 = 0
    for i in range(len(numList)):
        out1 = out1 + numList[i]
    return (out1)

def task2(*numlist):
    total = task1(*numlist)
    quotientAvg = total/(len(numlist))
    remainderAvg = total % (len(numlist))
    return int(quotientAvg), math.ceil(remainderAvg)

def task3(*numlist):
    resultlist = []
    for i in range(len(numlist)):
        if numlist[i] % 2 == 0:
            resultlist.append(numlist[i])
    return(resultlist)

def task4(*numlist):
    smallest = numlist[0]
    position = 0
    for i in range(len(numlist)):
        if numlist[i] < smallest:
            smallest = numlist[i]
            position = i
    return(smallest,position+1)


        
inArray = (72,111,63,85,61,56,118,121,61,69,63,61)
result1 = task1(*inArray)
print(result1)
result2 = task2(*inArray)
print(result2)
result3 = task3(*inArray)
print(result3)
result4 = task4(*inArray)
print(result4)