class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1

        answer = 0

        while left <= right:
            if people[left] + people[right] > limit:

                right -= 1
            else:
                left += 1
                right -= 1
            answer += 1
        # [1,2,2,3,3] 3
        # l    r
        return answer