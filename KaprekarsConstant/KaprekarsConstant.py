#!/usr/bin/python3

def largest(List):
    Max = 0
    loop = 0
    out = 0
    for current in List:
        if current > Max:
            Max = current
            out = loop
        loop += 1
    return out + 1

def smallest(List):
    Max = 999999999999999
    loop = 0
    out = 0
    for current in List:
        if current < Max:
            Max = current
            out = loop
        loop += 1
    return out + 1

def inputs(num): 
    List = []
    for each in str(num):
        List += [int(each)]

    large = ""
    tmpList = List
    while len(large) < 4:
        L = largest(tmpList)
        large += str(tmpList[L -1])
        del tmpList[L -1]

    List = []
    for each in str(num):
        List += [int(each)]

    small = ""
    tmpList = List
    while len(small) < 4:
        L = smallest(tmpList)
        small += str(tmpList[L -1])
        del tmpList[L -1]

    return large, small

def KaprekarsConstant(num):
    large, small = inputs(num)
    loop = 0
    while True:
        loop += 1
        i = int(large) - int(small)
        if i == 6174:
            return loop
        large, small = inputs(i)
    
# keep this function call here
while True:
    inp = input(": ")
    if len(inp) != 4:
        print ("Error: bad input")
    else:
        break
print(KaprekarsConstant(inp))

