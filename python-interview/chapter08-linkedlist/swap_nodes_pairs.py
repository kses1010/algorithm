# 24. Swap Nodes in Pairs


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 단순 값 교환
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    # 반복문 스왑
    def swap_pairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            p = head.next
            head.next = p.next
            p.next = head

            prev.next = p

            head = head.next
            prev = prev.next.next

        return root.next

    # 재귀 스왑
    def swap_recur(self, head: ListNode):
        if head and head.next:
            p = head.next
            # 스왑된 값 리턴 받음
            head.next = self.swap_recur(p.next)
            p.next = head
            return p
        return head
