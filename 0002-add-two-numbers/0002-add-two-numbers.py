# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        result = dummy
        #print(current)
        # while current:
        #     print(current.val)
        #     current = l1.next
        carry = 0
        l1_curr = l1
        l2_curr = l2
        
       
        while l1_curr or l2_curr or carry:
            val1 = 0
            val2 = 0
           
            if l1_curr:
                val1 = l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr:
                val2 = l2_curr.val
                l2_curr = l2_curr.next
                
            dig_sum = val1 + val2 + carry
            
        

            res = dig_sum%10
            carry = dig_sum//10
            

            
            
            result.next = ListNode(res)
            result=result.next    
        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna