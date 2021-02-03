# 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


sol = Solution()
s1, t1 = 'anagram', 'nagaram'
s2, t2 = 'rat', 'car'
print(sol.isAnagram(s1, t1))
