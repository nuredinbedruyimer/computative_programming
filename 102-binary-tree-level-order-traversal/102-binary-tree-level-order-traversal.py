# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        queue=collections.deque()
        queue.append(root)
        while queue:
            lengthOfQueue=len(queue)
            levelValues=[]
            for i in range(lengthOfQueue):
                node=queue.popleft()
                if node:
                    levelValues.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levelValues:
                answer.append(levelValues)
        return answer
                