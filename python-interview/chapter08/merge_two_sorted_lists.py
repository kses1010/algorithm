class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.data > l2.data):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

    def merge_iteratively(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]

sol = Solution()
print(sol.merge_iteratively(l1, l2))
