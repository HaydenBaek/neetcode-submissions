

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        longest = 1

        for right in range(1, len(arr)):
            current = self.compare(arr[right - 1], arr[right])

            # Equal values cannot be part of a turbulent sequence.
            if current == 0:
                left = right

            # Check whether the previous and current comparisons alternate.
            elif right >= 2:
                previous = self.compare(arr[right - 2], arr[right - 1])

                # Same direction means turbulence was broken.
                if previous == current:
                    left = right - 1

            longest = max(longest, right - left + 1)

        return longest

    def compare(self, a: int, b: int) -> int:
        if a < b:
            return 1
        if a > b:
            return -1
        return 0