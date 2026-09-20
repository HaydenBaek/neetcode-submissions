class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        

        counter = Counter(chars)
        answer = 0
        for word in words:
            counter_1 = counter.copy()
            done = True

            print(counter_1)

            for c in word:
                
                if c in counter_1 and counter_1[c] > 0:
                    counter_1[c] -= 1
                    
                else:
                    done = False
                    break

            if done:
                answer += len(word)
        
        return answer
            


