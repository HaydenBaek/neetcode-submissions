# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        return_list = ListNode()
        head = return_list
        carry = 0
        while l1 or l2 or carry:
            curr_sum = 0
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            curr_sum += carry

            if curr_sum >= 10:
                curr_sum = curr_sum % 10
                carry = 1
            else:
                carry = 0
            return_list.next = ListNode(curr_sum)
            return_list = return_list.next
        
        return head.next