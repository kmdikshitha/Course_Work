# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def findTreasure(head):
    if not head:
        return True
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next   
        fast = fast.next.next   
        
        if slow == fast: 
            return False
    
    return True


# head1 = ListNode(2)
# head1.next = ListNode(1)
# head1.next.next = ListNode(0)
# head1.next.next.next = ListNode(10)
# head1.next.next.next.next = head1.next 
# print(findTreasure(head1))


# head2 = ListNode(20)
# head2.next = ListNode(-1)
# head2.next.next = head2
# print(findTreasure(head2))

# head3 = ListNode(12)
# print(findTreasure(head3))
