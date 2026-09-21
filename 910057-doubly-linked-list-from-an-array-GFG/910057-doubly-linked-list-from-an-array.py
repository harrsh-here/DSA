''' class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''

class Solution:
    
    
    def createDLL(self, arr):
        if not arr:
            return None
    
    # Initialize head with the first element
        self.head = Node(arr[0])
        curr = self.head
        
        # Append each remaining element in O(1) time per element
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            curr.next = new_node
            new_node.prev = curr
            curr = new_node  # Advance pointer to the tail
            
        return self.head
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna