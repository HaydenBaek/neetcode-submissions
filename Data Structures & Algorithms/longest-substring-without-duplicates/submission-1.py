class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = deque()
        longest = 0
        left = 0
        for right in range(len(s)):

            while s[right] in window:
                window.popleft()
                left += 1
            window.append(s[right])
            longest = max(longest, right - left + 1)
            
        return longest
        