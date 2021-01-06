import functools
from operator import mul


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 전가산기 풀이법
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

    # 역순 연결 리스트
    def reverse_list(self, head: ListNode):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

    # 연결리스트 -> python 리스트로 변환
    def to_list(self, node: ListNode):
        py_list = []

        while node:
            py_list.append(node.val)
            node = node.next
        return py_list

    # python 리스트 -> 역순 연결리스트 변환
    def to_reversed_linked_list(self, result: ListNode):
        prev = None

        for i in result:
            node = ListNode(i)
            node.next = prev
            prev = node

        return node

    def add_two_numbers(self, l1, l2):
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        result = int(''.join(str(i) for i in a)) + int(''.join(str(i) for i in b))

        return self.to_reversed_linked_list(str(result))


list1 = [1, 2, 3, 4, 5]
print(''.join(str(e) for e in list1))
print(''.join(map(str, list1)))
print(functools.reduce(lambda x, y: 10 * x + y, list1))
print(functools.reduce(mul, list1))
