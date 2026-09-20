class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        answer = 0
        current_length = 0
        left = 0
        seen = set()

        for right in range(len(s)):
            char = s[right]

            if char in seen:


                while left < right and s[left] != char:
                    seen.remove(s[left])
                    left += 1
                    current_length -= 1
                left += 1
            else:
                current_length += 1
                answer = max(answer, current_length)
                seen.add(char)
        return answer

