# 148. Sort List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        p = head
        list_n = []
        while p:
            list_n.append(p.val)
            p = p.next

        list_n.sort()

        p = head
        for i in range(len(list_n)):
            p.val = list_n[i]
            p = p.next
        return head
