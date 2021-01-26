# 105. Construct Binary Tree from Preorder and Inorder Traversal
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            # 전위 순회 결과는 중위 순회 분할 인덱스다.
            index = inorder.index(preorder.pop(0))

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node

    def build_tree(self, inorder, postorder):
        if inorder:
            # 후위 순회 pop 결과는 중위 순회 분할 인덱스
            index = inorder.index(postorder.pop())

            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.right = self.build_tree(inorder[index + 1:], postorder)
            node.left = self.build_tree(inorder[:index], postorder)

            return node
