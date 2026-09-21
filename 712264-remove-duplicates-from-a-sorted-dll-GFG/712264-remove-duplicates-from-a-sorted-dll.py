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
       
       
        while curr and curr.next:
           if curr.data == curr.next.data:
               next_node = curr.next.next
               curr.next = next_node
               if next_node:
                   next_node.prev = curr
           else:
                curr = curr.next
        return headRef
               

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna