# 819. Most Common Word
import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = [i for i in re.sub(r'[^\w]', ' ', paragraph).lower().split() if i not in banned]
        counter = collections.Counter(word_list)

        return counter.most_common(1)[0][0]


paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
banned1 = ["hit"]
sol = Solution()
print(sol.mostCommonWord(paragraph1, banned1))
