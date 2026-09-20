# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def bfs(root:Optional[TreeNode]):

            result = []

            if not root:
                return

            q = deque()

            q.append(root)

            while q:

                node = q.popleft()

                level = []

                if node:

                    level.append(node.val)

                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
            
                if level:
                    result.append(level)


            return result
        
        return bfs(p) == bfs(q)
 
            