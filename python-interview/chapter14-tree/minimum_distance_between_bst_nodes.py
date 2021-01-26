# 783. Minimum Distance Between BST Nodes
import sys
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        prev = -sys.maxsize
        result = sys.maxsize

        def dfs(node):
            if node.left:
                dfs(node)
            nonlocal prev, result
            result = min(result, node.val - prev)
            prev = node.val

            if node.right:
                dfs(node.right)

        dfs(root)
        return result

    def min_diff_in_bst(self, root):
        pre_val = -inf
        answer = inf

        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            answer = min(answer, node.val - pre_val)
            pre_val = node.val

            node = node.right
        return answer
