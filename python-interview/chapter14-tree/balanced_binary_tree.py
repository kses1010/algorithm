# 110. Balanced Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 한 번이라도 자식노드 왼쪽, 오른쪽 차이가 1보다 크면 -1로 결정하여 회복이 되지않도록 한다.
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        # -1이면 균형 이진트리가 아니다.
        return dfs(root) != -1
