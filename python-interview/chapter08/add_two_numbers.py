import functools
from operator import mul


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        # 자리 올림수
        carry = 0
        while l1 or l2 or carry:
            val_sum = 0
            # 두 입력값의 합 계산
            if l1:
                val_sum += l1.val
                l1 = l1.next
            if l2:
                val_sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(val_sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next


list1 = [1, 2, 3, 4, 5]
print(''.join(str(e) for e in list1))
print(''.join(map(str, list1)))
print(functools.reduce(lambda x, y: 10 * x + y, list1))
print(functools.reduce(mul, list1))
