# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root1,root2,depth):
            
            if  root1 is None and root2 is None :
                return None
            if depth%2:
                temp=root1.val
                root1.val=root2.val
                root2.val=temp
            print(depth)
            helper(root1.left,root2.right,depth+1)
            helper(root1.right,root2.left,depth+1)
            
        helper(root.left,root.right,1)
        return root
        
        