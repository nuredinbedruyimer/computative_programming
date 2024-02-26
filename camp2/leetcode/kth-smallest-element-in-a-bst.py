# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[k]
        x = [0]
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans[0]-=1
            if ans[0]==0:
                x[0] = root.val
                return
            dfs(root.right)
        dfs(root)
    
        return x[0]

        