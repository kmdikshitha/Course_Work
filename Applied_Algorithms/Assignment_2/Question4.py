def largestArea(blocks):
    maxArea = 0
    n = len(blocks)
    
    for i in range(n):
        minHeight = blocks[i]
        for j in range(i, n):
            minHeight = min(minHeight, blocks[j])
            width = j - i + 1
            area = minHeight * width
            maxArea = max(maxArea, area)
    
    return maxArea

# print(largestArea([1,3,2,5,4]))
# print(largestArea( [3, 4, 5, 3, 5]))
# print(largestArea( [6, 2, 5, 4, 5, 1, 6]))
# print(largestArea( [5, 3, 7, 7, 2, 3, 8, 6, 4, 5, 9]))
# print(largestArea( [4, 1, 3, 4, 2, 4, 3, 5, 6]))
# print(largestArea( [7, 7, 7, 7, 7, 1, 2, 3, 4, 5]))
# print(largestArea([9, 6, 7, 8, 6, 7, 8, 6, 9]))
# print(largestArea( [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(largestArea
(
    [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        10000,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1
    ]
))

print(largestArea
(
    [
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1
    ]
))

        