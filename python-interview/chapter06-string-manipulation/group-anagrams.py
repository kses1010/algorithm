# 49. Group Anagrams
import collections


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return anagrams.values()


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]
sol = Solution()
print(sol.groupAnagrams(strs1))
print(sol.groupAnagrams(strs2))
print(sol.groupAnagrams(strs3))
