# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        
        # code here
        if not headRef:
            return None
        curr = headRef
        elem = curr
       
       
        while curr.next:
           if curr.data != elem.data:
               elem.next = curr
               
               curr.prev = elem
               elem = curr
           curr = curr.next
           
        if curr.data != elem.data:
               elem.next = curr
               
               curr.prev = elem
               elem = curr
        else:
            elem.next = None
        return headRef

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna