# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum = float("-inf")
    
        def pathSum(root):
            if not root:
                return 0
            
            leftMax = max(0, pathSum(root.left))
            rightMax = max(0, pathSum(root.right))
            self.maxPathSum = max(self.maxPathSum, leftMax + rightMax + root.val)
            return max(leftMax, rightMax) + root.val

        
        pathSum(root)
        return self.maxPathSum