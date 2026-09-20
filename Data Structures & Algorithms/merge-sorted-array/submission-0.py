class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0

        while index < n:
            nums1[m] = nums2[index]
            m += 1
            index += 1
        nums1.sort()
