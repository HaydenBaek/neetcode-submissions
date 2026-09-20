# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        maxInf = float("inf")
        minInf = float("-inf")

        def boundCheck(node, lowerBound, upperBound):
            if not node:
                return True
            
            if not lowerBound < node.val < upperBound:
                return False
            
            return boundCheck(node.left, lowerBound, node.val) and boundCheck(node.right, node.val, upperBound)
        
        return boundCheck(root, minInf, maxInf)
