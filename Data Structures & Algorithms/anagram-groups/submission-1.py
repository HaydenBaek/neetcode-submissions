class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        for string in strs:

            sort = ''.join(sorted(string))

            anagrams[sort].append(string)

        return list(anagrams.values())

        