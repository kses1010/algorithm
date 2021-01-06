class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 역순 연결리스트
def reverse_list(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next_node, node.next = node.next, prev
        prev, node = node, next_node

    return prev


# 구간별 역순 연결리스트
def reverse_list_select(head, n, m):
    if not head or n == m:
        return head

    root = start = ListNode(0)
    root.next = head

    for i in range(m - 1):
        start = start.next
    end = start.next

    for _ in range(m - n):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp

    return root.next
