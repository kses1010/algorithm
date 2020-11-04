

class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        result = []

        def dfs(idx, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(idx, len(digits)):
                for j in phone_number[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        phone_number = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        dfs(0, "")
        return result


sol = Solution()
num1 = "23"
num2 = "2"
print(sol.letterCombinations(num1))
print(sol.letterCombinations(num2))
