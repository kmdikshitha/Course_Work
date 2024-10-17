def treasure_seq(target, n):
    operations = []
    targetIndex = 0
    
    for i in range(1, n + 1):
        if targetIndex >= len(target):
            break
        
        operations.append("Push")
        
        if target[targetIndex] == i:
            targetIndex += 1
        else:
            operations.append("Pop")
    
    return operations

# target = [1, 2,3]
# n = 3
# print(treasure_seq(target, n))