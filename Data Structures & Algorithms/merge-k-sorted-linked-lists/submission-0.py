# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nodes = []

        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()
        dummy = ListNode()
        current = dummy
        for node in nodes:
            newNode = ListNode(node)
            current.next = newNode
            current = current.next
        return dummy.next