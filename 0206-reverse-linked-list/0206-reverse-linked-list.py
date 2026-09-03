class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print(head)
        if head == None:
            return head

        curr = head
        prev = None

        while curr.next:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        curr.next = prev
        head = curr

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna