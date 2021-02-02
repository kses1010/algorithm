# 336. Palindrome Pairs
from collections import defaultdict
from typing import List


class Solution:
    # 시간 초과
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        answer = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    answer.append([i, j])
        return answer


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word):
        return word[::] == word[::-1]

    def insert(self, index, word):
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - 1]):
                # 해당 글자가 트라이에서 팰린드롬이 존재할 경우
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index, word):
        result = []
        node = self.root

        while word:
            # 탐색 중간에 word_id가 있고 나머지 문자가 팰린드롬
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 끝까지 탐색했을 때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 끝까지 탐색했을 때 palindrome_word_ids 가 있는 경우
        for word_id in node.palindrome_word_ids:
            result.append([index, word_id])

        return result


class Solution2:
    def palindrome_pairs(self, words):
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        answers = []
        for i, word in enumerate(words):
            answers.extend(trie.search(i, word))

        return answers


sol = Solution()
sol2 = Solution2()
word_list = ["abcd", "dcba", "lls", "s", "sssll"]
print(sol.palindromePairs(word_list))
print(sol2.palindrome_pairs(word_list))
