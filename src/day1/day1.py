import math

def partOne():
    file = open("../day1input.txt", "r")
    previousNumber = math.inf
    currentNumber = 0
    count = 0
    
    for line in file:
        currentNumber = int(line)
        if (currentNumber > previousNumber):
            count = count + 1
        previousNumber = currentNumber
    
    print(count)
    file.close()
    
def partTwo():
    file = open("../day1input.txt", "r")
    first = int(file.readline())
    second = int(file.readline())
    windowOne = math.inf
    windowTwo = 0
    count = 0
    
    for line in file:
        third = int(line)
        windowTwo = first + second + third
        if (windowTwo > windowOne):
            count = count + 1
        first = second
        second = third
        windowOne = windowTwo
        
    print(count)
    file.close()