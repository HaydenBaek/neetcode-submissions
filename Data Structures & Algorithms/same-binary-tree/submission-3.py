# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def same(first, second):
            if not first and not second:
                return True

            if not first and second:
                return False
            if not second and first:
                return False

            if first.val != second.val:
                return False

            return same(first.left, second.left) and same(first.right, second.right)
        
        return same(p, q)