# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bucket_table = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char not in bucket_table:
                stack.append(char)
            elif not stack or bucket_table[char] != stack.pop():
                return False
        # 전부 정상적으로 유효한 괄호면 스택은 비워진다.
        return not stack


sol = Solution()
s1 = "()"
s2 = "()[]{}"
s3 = "(]"
s4 = "([)]"
s5 = "{[]}"
print()
print(sol.isValid(s1))
print(sol.isValid(s2))
print(sol.isValid(s3))
print(sol.isValid(s4))
print(sol.isValid(s5))
