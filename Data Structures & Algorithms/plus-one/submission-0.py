class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        stringNumber = ""
        for i in digits:
            stringNumber += str(i)
        intNumber = int(stringNumber) + 1
        numberAdded = str(intNumber)
        result = []
        index = 0
        while index < len(numberAdded):
            result.append(numberAdded[index])
            index += 1
        
        return result