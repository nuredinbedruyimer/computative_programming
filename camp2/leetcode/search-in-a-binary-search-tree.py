# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = [None]
        def dfs(node, data):
            if not node:
                return None
            if node.val==data:
                ans[0]=node
                return
            if node.val>data:
                dfs(node.left, data)
            elif node.val<data:
                dfs(node.right, data)
        dfs(root,val)
        return ans[0]