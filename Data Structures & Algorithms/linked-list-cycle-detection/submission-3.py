# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        check = set()

        current = head

        while current.next:

            if current.val in check:
                return True
            else:
                check.add(current.val)
            
            current = current.next
        
        return False
        