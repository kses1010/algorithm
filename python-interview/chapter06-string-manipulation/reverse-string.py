class Solution:
    def reverseString(self, s: [str]) -> None:
        s.reverse()


class Solution2:
    def reverseString2(self, s: [str]) -> None:
        s[:] = s[::-1]


str1 = ["h", "e", "l", "l", "o"]
str2 = ["H", "a", "n", "n", "a", "h"]

sol = Solution()
sol2 = Solution2()
# sol.reverseString(str1)
# sol.reverseString(str2)
sol2.reverseString2(str1)
sol2.reverseString2(str2)

print(str1)
print(str2)
