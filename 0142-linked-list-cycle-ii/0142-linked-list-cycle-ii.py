# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                sp = head
                while sp!=fp:
                    sp = sp.next
                    fp = fp.next
                return sp
        return None

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna