class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums_string = [str(num) for num in nums]

        answer = []

        while nums_string:
            max_index = 0
            for i in range(1, len(nums_string)):
                if nums_string[i] + nums_string[max_index] > nums_string[max_index] + nums_string[i]:
                    max_index = i
            answer.append(nums_string[max_index])
            nums_string.pop(max_index)
        result = "".join(answer)
        return result if result[0] != '0' else '0'
