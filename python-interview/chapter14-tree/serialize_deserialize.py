# 297. Serialize and Deserialize Binary Tree
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        q = deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)

                result.append((str(node.val)))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        # 예외처리 - root 값이 # 일 경우 트리구조가 아님.
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        q = deque([root])
        index = 2
        # 런너를 이용한 자식 노드 결과를 먼저 확인하고 난 뒤 큐 삽입
        while q:
            node = q.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            index += 1
        return root
