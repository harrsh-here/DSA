# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        # code here
        if not head:
            return None
        if not head.next and head.data == x:
            return None
        
        curr = head
        prev = None
        new_head = head
        
        while curr:
            
            if curr.data == x: 
                if curr.next:
                    curr.next.prev = prev
                if prev :
                    prev.next = curr.next
                if curr == new_head:
                    new_head = new_head.next
            else:
                prev = curr
            curr = curr.next
        return new_head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna