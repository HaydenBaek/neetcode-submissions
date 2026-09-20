class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToLetters = {
            "0": ["+"],
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


        result = [""]

        index = 0

        while index < len(digits):
            
            digit = digits[index]

            letters = numToLetters[digit]

            newList = []

            for combo in result:
                for char in letters:
                    newList.append(combo + char)
            
            result = newList
            index += 1

        return [] if result[0] == "" else result
        
