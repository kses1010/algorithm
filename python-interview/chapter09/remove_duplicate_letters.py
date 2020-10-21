import collections


class Solution:
    def removeDuplicateLetter(self, s: str) -> str:
        word_set = set()
        word_stack = []
        for char in s:
            if char in word_set:
                word_stack.remove(char)
            word_set.add(char)
            word_stack.append(char)
        return ''.join(word_stack)

    def remove_duplicate_recursively(self, s: str) -> str:
        # 집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]

            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.remove_duplicate_recursively(suffix.replace(char, ''))

        return ''

    def remove_duplicate_stack(self, s: str) -> str:
        counter, word_set, word_stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in word_set:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while word_stack and char < word_stack[-1] and counter[word_stack[-1]] > 0:
                word_set.remove(word_stack.pop())

            word_set.add(char)
            word_stack.append(char)

        return ''.join(word_stack)


sol = Solution()
s1 = "bcabc"
s2 = "cbacdcbc"
print(sol.removeDuplicateLetter(s1))
print(sol.removeDuplicateLetter(s2))
print(sol.remove_duplicate_recursively(s1))
print(sol.remove_duplicate_recursively(s2))
print(sol.remove_duplicate_stack(s1))
print(sol.remove_duplicate_stack(s2))

