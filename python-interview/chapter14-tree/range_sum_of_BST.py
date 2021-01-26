# 938. Range Sum of BST
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        return (root.val if low <= root.val <= high else 0) + \
               self.rangeSumBST(root.left, low, high) + \
               self.rangeSumBST(root.right, low, high)


class Solution2:
    def dfs_sum_bst(self, root, low, high):
        def dfs(node):
            if not node:
                return 0

            if node.left < low:
                return dfs(root.right)
            elif node.right > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)

    def bfs_sum_bst(self, root, low, high):
        q = deque([root])
        val_sum = 0

        while q:
            node = q.popleft()

            # BFS 탐색을 한다. low보다 크거나 high보다 작으면 전부 큐에 넣는다.
            if node:
                if node.val > low:
                    q.append(node.left)
                if node.val < high:
                    q.append(node.right)
                if low <= node.val <= high:
                    val_sum += node.val
        return val_sum
