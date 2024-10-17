class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Queue_LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val:int):
        product=Node(val)
        if self.tail:  
            self.tail.next = product 
        self.tail = product 
        if not self.head:  
            self.head = product 
            
    def dequeue(self):
        if not self.head:
            return -1
        removedProduct = self.head.val  
        self.head = self.head.next  
        if not self.head:  
            self.tail = None 
        return removedProduct

    def QueueToList(self)->list[int]:
        conveyorBelt=[]
        curr=self.head

        if curr is None:
            return conveyorBelt 

        while curr:
            conveyorBelt.append(curr.val)  
            curr = curr.next 
        return conveyorBelt
    
# queue = Queue_LL()
# commands = [["enqueue", 1], ["dequeue"], ["dequeue"], ["enqueue", 6], ["dequeue"]]
# commands = [["enqueue", i] for i in range(1, 100001)] + \
#            [["dequeue"] for _ in range(100001)] 
# commands =  [["enqueue", 1], ["enqueue", 2], ["enqueue", 3], ["dequeue"],
# ["enqueue", 4], ["dequeue"], ["dequeue"], ["enqueue", 6]]


# for command in commands:
#     if command[0] == "enqueue":
#         queue.enqueue(command[1])
#     elif command[0] == "dequeue":
#         queue.dequeue()

# print(queue.QueueToList())