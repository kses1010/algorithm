# 937. Reorder Data in Log Files
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        for i in logs:
            if i.split()[1].isalpha():
                letter.append(i)
            else:
                digit.append(i)

        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit


sol = Solution()
logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(sol.reorderLogFiles(logs1))
