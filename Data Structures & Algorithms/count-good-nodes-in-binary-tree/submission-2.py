# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        def dfs(node, path):
            nonlocal count
            if not node:
                return
            if all(node.val >= x for x in path):
                count += 1
            path.append(node.val)
            pathCopy = path.copy()
            dfs(node.left, path)
            dfs(node.right, pathCopy)
        if root.left:
            dfs(root.left, [root.val])
        if root.right:
            dfs(root.right, [root.val])
        return count