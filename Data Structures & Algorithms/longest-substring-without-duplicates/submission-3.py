class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        window = set()
        index = 0
        left = 0 

        while index < len(s):

            while s[index] in window and index < len(s):
                window.remove(s[left])
                left += 1

            window.add(s[index])
            length = max(length, len(window))
            index += 1
        return length
        