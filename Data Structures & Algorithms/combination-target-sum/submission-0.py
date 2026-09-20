class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        finalList = []

        #currentpath = [2,2,...]
        def backtrack(currentPath, currentList, sum1):

            if sum1 == target:
                finalList.append(currentPath)
                return
            elif sum1 > target:
                #greater than the target
                return
            else:
                #less than target
                for i in range(len(currentList)):
                    sum1 += currentList[i]
                    backtrack(currentPath + [currentList[i]], currentList[i:], sum1)
                    sum1 -= currentList[i]
            
        backtrack([], nums, 0)
        return finalList
        