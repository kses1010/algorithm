class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result


sol = Solution()
s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "ac"
print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
print(sol.longestPalindrome(s3))
print(sol.longestPalindrome(s4))
