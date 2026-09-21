''' Structure of Doubly Linked List Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insert_at_head(self, val,head):              # O(1)
        new_node = Node(val)
        new_node.next = head
        if head:
            head.prev = new_node
        head = new_node
        

    

    
        
    def insertAtPos(self, head, p, x):
        # Code Here
        index = p
        val = x
        # if index == 0:
        #     self.insert_at_head(val,head)
        #     return head
        new_node = Node(val)
        curr = head
        count = 0
        while curr and count< index:
            curr = curr.next
            count += 1
        if not curr:
            print("Index out of range")
            return
        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node
        new_node.prev = curr
        # Only set .prev on next_node if it isn't None
        if next_node:
            next_node.prev = new_node
        return head
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna