# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        def insert(node):
            if not node:
                return
            
            if val < node.val and not node.left:
                new_node = TreeNode(val)
                node.left = new_node
            elif val > node.val and not node.right:
                new_node = TreeNode(val)
                node.right = new_node
            else:
                if val < node.val:
                    insert(node.left)
                else:
                    insert(node.right)
            return
        insert(root)
        return root
