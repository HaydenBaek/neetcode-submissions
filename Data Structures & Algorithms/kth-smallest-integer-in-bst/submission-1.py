# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        current = root
        stack = []

        while stack or current:
            
            #keep going left
            while current:
                stack.append(current)
                current = current.left
            
            k -= 1
            current = stack.pop()
            if k == 0:
                return current.val

            current = current.right