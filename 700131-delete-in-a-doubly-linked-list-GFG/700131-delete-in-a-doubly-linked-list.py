""" Structure of a Doubly Linked List Node
class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None
"""


class Solution:
    def delete_head(self,head):
        # if head is empty
        if not head:  # NO head, No deletion
            return head
        elif not head.next:  # no next element, remove head reference
            temp = head
            head = None
            del temp
        else:
            temp = head
            head = head.next
            head.prev = None
            del temp
        return head

    def delPos(self, head, x):
        # code here
        
        if not head:
            # print("List is empty")
            return head
        # if index is 1 means delete head
        if x == 1 :
            return self.delete_head(head)
        else:
            curr = head
            count = 1
            while curr and count < x - 1 :
                curr = curr.next
                count += 1
            temp = curr.next
            # if not curr.next:
            next_node = curr.next.next
            curr.next = next_node
            if next_node:
                next_node.prev = curr
            del temp
        return head


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna