# 783. Minimum Distance Between BST Nodes
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = -inf
    result = inf

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

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
