def arrangePerformers(nums):
    performers=nums
    performers.sort()
    backstage = []
    
    for performer in reversed(performers):
        if backstage:
           backstage.insert(0, backstage.pop())
        backstage.insert(0, performer)
    
    return backstage

# # Example usage:
# nums = [17, 13, 11, 2, 3, 5, 7]
# # nums=[1000,1]
# output = arrangePerformers(nums)
# print(output)
