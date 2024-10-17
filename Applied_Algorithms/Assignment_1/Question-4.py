def findPowerLevels(powerLevels):
    res = [1] * len(powerLevels)
    
    leftRes = 1
    for i in range(len(powerLevels)):
        res[i] = leftRes
        leftRes *= powerLevels[i]

    rightRes = 1
    for j in range(len(powerLevels)-1, -1, -1):
        res[j] *= rightRes
        rightRes *= powerLevels[j]
    
    return res

# print(findPowerLevels([1, 2, 3, 4])) 
# print(findPowerLevels([-1,1,0,-3,3]))  
