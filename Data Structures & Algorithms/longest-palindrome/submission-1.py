class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        counter = Counter(s)

        sorted_items = counter.most_common()

        answer = 0
        hasOdd = False
        for item, count in sorted_items:
            
            add = count - (count % 2)
            
            answer += add
            
            if count % 2 == 1:
                hasOdd = True
        
        if hasOdd:
            answer += 1

        return answer
