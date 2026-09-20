class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        changes = defaultdict(int)

        for bill in bills:
            if bill != 5:
                if bill == 10:
                    if changes[5] < 1:
                        return False
                    else:
                        changes[5] -= 1
                        
                elif bill == 20:
                    if not (changes[10] >= 1 and changes[5] >= 1) and not (changes[5] >= 3):
                        return False
                    else:
                        if changes[10] >= 1 and changes[5] >= 1:
                            changes[10] -= 1
                            changes[5] -= 1
                        else:
                            changes[5] -= 3
            changes[bill] += 1
        
        return True