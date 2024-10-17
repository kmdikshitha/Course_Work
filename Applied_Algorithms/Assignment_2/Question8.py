class quarryPieLine:
    def __init__(self):
        self.customers_stack = []  
        self.customer_counter = 0   

    def joinInFront(self):
        self.customer_counter += 1
        self.customers_stack.insert(0, self.customer_counter) 

    def joinInMiddle(self):
        self.customer_counter += 1
        if len(self.customers_stack) == 0:
            self.customers_stack.append(self.customer_counter)
        else:
            middle_index = len(self.customers_stack) // 2
            self.customers_stack.insert(middle_index, self.customer_counter) 

    def joinInBack(self):
        self.customer_counter += 1
        self.customers_stack.append(self.customer_counter) 

    def removeFromFront(self):
        if len(self.customers_stack) > 0:
            self.customers_stack.pop(0)  

    def removeFromMiddle(self):
        if len(self.customers_stack) > 0:
            middle_index = (len(self.customers_stack) - 1) // 2
            self.customers_stack.pop(middle_index)  
    def removeFromBack(self):
        if len(self.customers_stack) > 0:
            self.customers_stack.pop()  
    def whoIsFront(self) -> int:
        if len(self.customers_stack) > 0:
            return self.customers_stack[0]
        else:
            return -1 

    def whoIsMiddle(self) -> int:
        if len(self.customers_stack) == 0:
            return -1 
        else:
            middle_index = (len(self.customers_stack) - 1) // 2
            return self.customers_stack[middle_index] 

    def whoIsBack(self) -> int:
        if len(self.customers_stack) > 0:
            return self.customers_stack[-1] 
        else:
            return -1 



# commands = [   2,
#     7,
#     8,
#     9,
#     1,
#     3,
#     2,
#     7,
#     8,
#     9,
#     2,
#     3,
#     5,
#     6,
#     7,
#     8,
#     9]
# output = []
# qpl = quarryPieLine()

# for cmd in commands:
#     if cmd == 1:
#         qpl.joinInFront()
#     elif cmd == 2:
#         qpl.joinInMiddle()
#     elif cmd == 3:
#         qpl.joinInBack()
#     elif cmd == 5:
#         qpl.removeFromMiddle()
#     elif cmd == 6:
#         qpl.removeFromBack()
#     elif cmd == 7:
#         output.append(qpl.whoIsFront())
#     elif cmd == 8:
#         output.append(qpl.whoIsMiddle())
#     elif cmd == 9:
#         output.append(qpl.whoIsBack())

# print(output)

# # [
# #     1,
# #     1,
# #     1,
# #     2,
# #     4,
# #     3,
# #     2,
# #     4,
# #     3
# # ]