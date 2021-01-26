# 연결리스트
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# 전위 순회
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


# 중위 순회
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


# 후위 순회
def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)
