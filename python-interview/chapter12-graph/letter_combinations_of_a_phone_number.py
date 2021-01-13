# 17. Letter Combinations of a Phone Number


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

    def letter_combinations(self, digits):
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        answer = []

        # 백트래킹(like dfs)
        def backtrack(combination, next_digit):
            # 끝에 도달하면 조합은 answer 추가
            if not next_digit:
                answer.append(combination)
            else:
                # 숫자 입력부터 차례로 탐색
                for i in phone[next_digit[0]]:
                    backtrack(combination + i, next_digit[1:])

        if digits:
            backtrack("", digits)
        return answer


sol = Solution()
num1 = "23"
num2 = "2"
print(sol.letterCombinations(num1))
print(sol.letter_combinations(num1))
print(sol.letterCombinations(num2))
