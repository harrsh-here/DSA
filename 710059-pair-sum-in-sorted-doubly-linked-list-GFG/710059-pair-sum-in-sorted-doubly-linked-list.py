# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        res =  []
        curr = head
        while curr.next:
            curr = curr.next
        p = head
        q = curr
        
        while p and q and p.data<q.data:
            total = p.data +q.data
            if total == target:
                res.append([p.data,q.data])
                p = p.next
                q = q.prev
            if total < target:
                p = p.next
            if total > target:
                q = q.prev
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna