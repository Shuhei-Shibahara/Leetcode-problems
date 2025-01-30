# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        resDepth = 1

        queue = deque([root])
        depth = 1

        while queue:
            currSum = 0
            for _ in range(len(queue)): #this is important in a DFS to now how to remove each level
                node = queue.popleft()
                currSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if currSum > maxSum:
                maxSum = currSum
                resDepth = depth
            
            depth += 1
        
        return resDepth


        