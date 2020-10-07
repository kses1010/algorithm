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


str1 = "A man, a plan, a canal: Panama"
str2 = "race a car"
sol1 = Solution()

if sol1.isPalindrome(str1):
    print(True)
else:
    print(False)

if sol1.isPalindrome(str2):
    print(True)
else:
    print(False)
