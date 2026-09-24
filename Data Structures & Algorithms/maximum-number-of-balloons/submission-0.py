class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        

        counter = Counter(text)

        count = 0
        exist = True
        balloon = "balloon"
        while exist:

            for c in balloon:
                if c in counter:
                    counter[c] -= 1
                else:
                    return count
                
                if counter[c] < 1: 
                    del counter[c]
            count += 1
        
        return count