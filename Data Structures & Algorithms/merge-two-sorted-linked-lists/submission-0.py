# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        addings = dummy

        while list1 and list2:

            if list1.val < list2.val:
                addings.next = list1
                list1 = list1.next
            else:
                addings.next = list2
                list2 = list2.next
            
            addings = addings.next
        
        if list1:
            addings.next = list1
        elif list2:
            addings.next = list2
        
        return dummy.next
