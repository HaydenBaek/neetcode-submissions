class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        counter = defaultdict(list)
        seen = set()
        for i, n in enumerate(nums):
            if n in seen:
                difference = abs(counter[n][-1] - i)
                if difference <= k:
                    return True    
            else:
                seen.add(n)
           
            counter[n].append(i)

        return False
