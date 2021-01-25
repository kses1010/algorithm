# 687. Longest Univalue Path

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        longest = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.right:
                right += 1
            else:
                right = 0

            nonlocal longest
            longest = max(longest, left + right)
            return max(left, right)

        dfs(root)
        return longest
