# 424. Longest Repeating Character Replacement
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counter = collections.Counter()
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            common_char = counter.most_common(1)[0][1]

            if right - left - common_char > k:
                counter[s[left]] -= 1
                left += 1
        return right - left


s1 = "ABAB"
s2 = "AABABBA"
s3 = "AAABBC"
sol = Solution()
# print(sol.characterReplacement(s1, 2))
print(sol.characterReplacement(s2, 1))
# print(sol.characterReplacement(s3, 2))
