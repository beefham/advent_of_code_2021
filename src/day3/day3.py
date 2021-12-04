LENGTH_OF_LINE = 12

def partOne():
    file = open("day3input.txt", 'r')
    lines = file.readlines()
    gamma = getGamma(lines)
    integerGamma = int(gamma, 2)
    integerEpsilon = int(getEpsilon(gamma), 2)
    print(integerGamma * integerEpsilon)
    file.close()

def partTwo():
    file = open("day3input.txt", 'r')
    lines = file.readlines()
    oxygen = getOxygen(lines, 0)
    carbon = getCO2(lines, 0)
    intOxygen = int(oxygen, 2)
    intCarbon = int(carbon, 2)
    print(intOxygen * intCarbon)
    file.close()
    
def getBitAtPosition(string: str, position: int) -> str:
    return string[position]

def findMostCommonBit(lines, position: int) -> str:
    numberOfOnes = 0
    numberOfZeroes = 0
    for line in lines:
        bit = getBitAtPosition(line, position)
        if (bit == "1"):
            numberOfOnes += 1    
        elif (bit == "0"):
            numberOfZeroes += 1
        else:
            raise ValueError("Should be 0 or 1")
    return "1" if numberOfOnes >= numberOfZeroes else "0"

def findLeastCommonBit(lines, position: int) -> str:
    numberOfOnes = 0
    numberOfZeroes = 0
    for line in lines:
        bit = getBitAtPosition(line, position)
        if (bit == "1"):
            numberOfOnes += 1    
        elif (bit == "0"):
            numberOfZeroes += 1
        else:
            raise ValueError("Should be 0 or 1")
        
    # Zero has priority: if number of 0s = number of 1s return 0
    return "1" if numberOfOnes < numberOfZeroes else "0"
    
def getGamma(lines) -> str:
    gamma = ""
    for i in range(LENGTH_OF_LINE):
        bit = findMostCommonBit(lines, i)
        gamma = gamma + bit
    return gamma
        
def getEpsilon(gamma: str) -> str:
    epsilon = ""
    for char in gamma:
        bit = flipBit(char)
        epsilon = epsilon + bit
    return epsilon

def getOxygen(lines, position) -> str:
    if len(lines) <= 1:
        return lines[0] # base case
    if position >= LENGTH_OF_LINE:
        return lines[0] # base case
    
    bit = findMostCommonBit(lines, position)
    filteredLines = list(filter(lambda line: line[position] == bit, lines))
    return getOxygen(filteredLines, position + 1)

def getCO2(lines, position) -> str:
    if len(lines) <= 1:
        return lines[0] # base case
    
    if position >= LENGTH_OF_LINE:
        return lines[0] # base case
    
    bit = findLeastCommonBit(lines, position)
    filteredLines = list(filter(lambda line: line[position] == bit, lines))
    return getCO2(filteredLines, position + 1)
    
def flipBit(bit: str) -> str:
    if bit == "0":
        return "1"
    elif bit == "1":
        return "0"
    else:
        raise ValueError("Bit should be 0 or 1")