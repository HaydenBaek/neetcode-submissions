class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        # STEP 1: Find the correct row
        top, bottom = 0, rows - 1
        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        else:
            # target not in any row range
            return False

        # STEP 2: Binary search inside that row
        left, right = 0, cols - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
