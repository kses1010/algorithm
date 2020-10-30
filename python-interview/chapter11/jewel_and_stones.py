import collections


class Solution:
    def __init__(self):
        self.count = 0

    def numJewelsInStones(self, J: str, S: str) -> int:
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    self.count += 1
        return self.count

    def hash_table_sol(self, J: str, S: str) -> int:
        freqs = {}
        count = 0
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in J:
            if char in freqs:
                count += freqs[char]

        return count

    def dict_hash_sol(self, J: str, S: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0
        for char in S:
            freqs[char] += 1

        for char in J:
            count += freqs[char]

        return count

    def counter_hash_sol(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)
        count = 0
        print(freqs)
        for char in J:
            count += freqs[char]
        return count

    def pythonic_way_sol(self, J: str, S: str) -> int:
        return sum(s in J for s in S)


sol = Solution()
j1, s1 = "aA", "aAAbbbb"
j2, s2 = "z", "ZZ"
print(sol.numJewelsInStones(j1, s1))
print(sol.numJewelsInStones(j2, s2))
print(sol.dict_hash_sol(j1, s1))
print(sol.counter_hash_sol(j1, s1))
