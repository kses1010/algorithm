# 543. Diameter of Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest = 0

        def dfs(node):
            if not node:
                return -1
            # 왼쪽, 오른쪽 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            nonlocal longest
            longest = max(longest, left + right + 2)
            # 상태값
            return max(left, right) + 1

        dfs(root)
        return longest
