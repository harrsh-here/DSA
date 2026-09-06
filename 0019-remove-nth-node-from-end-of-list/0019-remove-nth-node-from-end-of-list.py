# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head 
        length = 0
        
        while curr:
            length+=1
            curr = curr.next
        if length == n:
            temp = head
            head = head.next
            del temp
            return head
        curr = head
        count = length - n
 
        
        for i in range(1,count):
            curr = curr.next

 
        curr.next = curr.next.next
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna