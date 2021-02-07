# 76. Minimum Window Substring
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        word_counter = collections.Counter(t)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            # 만약 word_counter[char]이 0보다 작으면 무시
            missing -= word_counter[char] > 0
            word_counter[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동
            if missing == 0:
                while left < right and word_counter[s[left]] != 0:
                    word_counter[s[left]] += 1
                    left += 1

                # 문자 길이 비교
                if not end or right - left < start - end:
                    start, end = left, right
                    word_counter[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]


sol = Solution()
s1, t1 = "ADOBECODEBANC", "ABC"
print(sol.minWindow(s1, t1))
