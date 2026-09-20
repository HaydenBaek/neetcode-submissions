# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        q = deque()

        q.append(root)
        answer = []

        while q:

            level = []

            for i in range(len(q)):

                node = q.popleft()

                if node:
                    level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if level:
                answer.append(level)

        bigList = []

        for i in answer:

            for j in i:
                bigList.append(j)
        
        bigList.sort()
        return bigList[k-1]
        


        