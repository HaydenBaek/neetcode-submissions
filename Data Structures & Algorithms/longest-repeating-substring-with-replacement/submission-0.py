class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        counter = defaultdict(int)
        left = 0
        right = 0
        size = 0

        while right < len(s):

            counter[s[right]] += 1

            #if the k - maxNum is smaller or equal to K. It is valid window
            max_num = max(counter.values())

            if right - left + 1 - max_num > k:
                counter[s[left]] -= 1
                left += 1
            
            size = max(size, right - left + 1)
            right += 1
            
        return size
