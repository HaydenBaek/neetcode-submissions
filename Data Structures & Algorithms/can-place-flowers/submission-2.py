class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0

        for mid in range(len(flowerbed)):

            left = mid - 1
            right = mid + 1

            left_eligible = False
            if left < 0 or flowerbed[left] == 0:
                left_eligible = True
            
            right_eligible = False
            if right == len(flowerbed) or flowerbed[right] == 0:
                right_eligible = True
            
            if left_eligible and flowerbed[mid] == 0 and right_eligible:
                flowerbed[mid] = 1
                n -= 1
        return n <= 0