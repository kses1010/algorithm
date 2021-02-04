# 240. Search a 2D Matrix II
import bisect
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, m - 1
        for i in range(n):
            if matrix[i][left] <= target <= matrix[i][right]:
                index = bisect.bisect_left(matrix[i], target)
                if matrix[i][index] == target:
                    return True
        return False

    def search_matrix(self, matrix, target):
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1

        return False

    def pythonic_search(self, matrix, target):
        return any(target in row for row in matrix)


sol = Solution()
matrix1 = [[1, 4, 7, 11, 15],
           [2, 5, 8, 12, 19],
           [3, 6, 9, 16, 22],
           [10, 13, 14, 17, 24],
           [18, 21, 23, 26, 30]]
print(sol.searchMatrix(matrix1, 5))
print(sol.searchMatrix(matrix1, 20))
print(sol.search_matrix(matrix1, 5))
print(sol.search_matrix(matrix1, 20))
