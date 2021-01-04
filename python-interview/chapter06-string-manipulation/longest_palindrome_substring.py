class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result

    def long_str(self, s):
        def two_point_slider(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 시간 더욱 단축시켜준다. 한글자이거나 단어 자체적으로 팰린드롬이라면 그대로 문자 출력
        if len(s) < 2 or s == s[::-1]:
            return s

        answer = ''
        for i in range(len(s)):
            # 짝수, 홀수
            answer = max(answer, two_point_slider(i, i), two_point_slider(i, i + 1), key=len)
        return answer


sol = Solution()
s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "bbbb"

print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
print(sol.longestPalindrome(s3))
print(sol.longestPalindrome(s4))
print("--------------")
print(sol.long_str(s1))
print(sol.long_str(s2))
print(sol.long_str(s3))
print(sol.long_str(s4))
