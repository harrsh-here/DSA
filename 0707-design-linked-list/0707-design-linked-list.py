class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        curr = self.head
        count = 0

        while curr and count < index:
            curr = curr.next
            count += 1

        if curr is None:
            return -1

        return curr.val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)

        # Empty list
        if self.head is None:
            self.head = new_node
            return

        curr = self.head

        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def addAtIndex(self, index, val):
        new_node = Node(val)

        # Insert at beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        count = 0

        # Find node at index-1
        while curr and count < index - 1:
            curr = curr.next
            count += 1

        # index is greater than length
        if curr is None:
            return

        new_node.next = curr.next
        curr.next = new_node

    def deleteAtIndex(self, index):
        
        # Empty list
        if self.head is None:
            return

        # Delete head
        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        # Find node at index-1
        while curr and count < index - 1:
            curr = curr.next
            count += 1

        # Invalid index
        if curr is None or curr.next is None:
            return

        # Delete index node
        curr.next = curr.next.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna