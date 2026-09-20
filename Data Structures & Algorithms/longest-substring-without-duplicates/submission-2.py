class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        window = deque()
        index = 0

        while index < len(s):

            while s[index] in window and index < len(s):
                window.popleft()
            window.append(s[index])
            length = max(length, len(window))
            index += 1
        return length
        