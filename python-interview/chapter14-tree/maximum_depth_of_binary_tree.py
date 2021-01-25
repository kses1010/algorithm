# 104. Maximum Depth of Binary Tree
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        depth = 0

        while q:
            depth += 1
            # 큐 연산 추출 노드의 자식 노드 삽입
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return depth
