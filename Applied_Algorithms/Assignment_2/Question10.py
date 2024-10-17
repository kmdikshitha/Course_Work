import random

class Node:
    def __init__(self, val):
        self.val = val  
        self.next = None
        self.down = None

class SkipList:
    def __init__(self):
        self.head = Node(-1) 
        self.levels = 0

    def search(self, target):
        curr = self.head
        while curr:
            while curr.next and curr.next.val < target:
                curr = curr.next
            if curr.next and curr.next.val == target:
                return True
            curr = curr.down
        return False

    def insert(self, num):
        stack = []
        curr = self.head
        
        while curr:
            while curr.next and curr.next.val < num:
                curr = curr.next
            stack.append(curr)
            curr = curr.down 
        
        insert_level = 0
        downNode = None 
        
        while stack:
            curr = stack.pop()
            newNode = Node(num)
            newNode.next = curr.next
            newNode.down = downNode
            curr.next = newNode
            downNode = newNode 
            

            insert_level += 1
            if random.random() > 0.5:
                break 

            if insert_level > self.levels:
                newHead = Node(-1)  
                newHead.down = self.head  
                self.head = newHead 
                self.levels += 1
        return None
# # Example usage:
# sl = SkipList()
# sl.insert(1)  # None
# sl.insert(2)  # None
# sl.insert(3)  # None
# print(sl.search(4))  # False
# sl.insert(4)  # None
# print(sl.search(4))  # True
# print(sl.search(1))  # True

# # Example usage for testing:
# sl = SkipList()
# print(sl.insert(1))  # None
# print(sl.insert(2))  # None
# print(sl.insert(3))  # None
# print(sl.search(4))  # False
# print(sl.insert(4))  # None
# print(sl.search(4))  # True
# print(sl.search(1))  # True

sl = SkipList()
results = []

    # Perform the operations and store the results
results.append(sl.insert(10))  # None
results.append(sl.insert(20))  # None
results.append(sl.insert(30))  # None
results.append(sl.insert(40))  # None
results.append(sl.search(15))   # Should return False
results.append(sl.insert(15))    # None
results.append(sl.search(15))    # Should return True
results.append(sl.search(25))    # Should return False
results.append(sl.insert(25))    # Noneresults.append(sl.search(25))    # Should return True
results.append(sl.insert(50))    # None
results.append(sl.search(50))    # Should return True
results.append(sl.insert(60))    # None
results.append(sl.search(10))    # Should return True
results.append(sl.search(60))    # Should return True
results.append(sl.search(70))    # Should return False

    # Print the results
print(results)