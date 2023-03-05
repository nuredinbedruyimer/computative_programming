# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer=[]
        def postorder(root,answer):
            if root is None:
                return answer
            else:
                answer= postorder(root.left,answer)
                answer.append(root.val)
                answer=postorder(root.right,answer)
                
                return answer 
            
        return postorder(root,answer)
        