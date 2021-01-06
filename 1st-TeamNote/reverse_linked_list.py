class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next_node, node.next = node.next, prev
        prev, node = node, next_node

    return prev
