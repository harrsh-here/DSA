class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        curr_odd = head
        even_head = curr_odd.next
        curr_even = even_head
        while curr_odd.next and curr_even.next:
            curr_odd.next = curr_even.next
            curr_odd = curr_even.next

            curr_even.next = curr_odd.next
            curr_even = curr_even.next
        curr_odd.next = even_head

        return head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna