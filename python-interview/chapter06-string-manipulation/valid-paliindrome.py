# 125. Valid Palindrome

import re
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strings = deque()
        for char in s:
            if char.isalnum():
                strings.append(char.lower())

        while len(strings) > 1:
            if strings.popleft() != strings.pop():
                return False

        return True

    def is_palindrome_slice(self, s):
        s = s.lower()
        # regex filter
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]  # 슬라이싱


str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"

sol = Solution()
print(sol.isPalindrome(str1))
print(sol.isPalindrome(str2))
print(sol.is_palindrome_slice(str1))
print(sol.is_palindrome_slice(str2))
