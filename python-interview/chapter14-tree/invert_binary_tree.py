# 226 Invert Binary Tree
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)
        return root

    def recur_invert_tree(self, root):
        if root:
            root.left, root.right = self.recur_invert_tree(root.right), \
                                    self.recur_invert_tree(root.left)
            return root
        return None
