class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longestSubString = 0
        left = 0
        right = 0
        length = 0
        visited = set()
        while right < len(s):
            if s[right] not in visited:
                length += 1
                visited.add(s[right])
                right += 1
            else:
                visited.remove(s[left])
                left += 1
            longestSubString = max(longestSubString, right - left)

        return longestSubString