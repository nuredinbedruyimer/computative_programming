# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            lengthOfQueue=len(queue)
            levelValues=[]
            total=0
            for i in range(lengthOfQueue):
                node=queue.popleft()
                if node:
                    total+=node.val
                    levelValues.append(node.val)
                    
                    queue.append(node.left)
                    queue.append(node.right)
            if levelValues:
                answer.append(total/len(levelValues))
            
        
        
        return answer
        