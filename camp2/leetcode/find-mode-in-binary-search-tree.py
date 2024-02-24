# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        memo={}
        def dfs(root):
            if not root:
                return 0
            if root.val in memo:
                memo[root.val]+=1
            else:
                memo[root.val]=1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        max_occurence=max(memo.values())
        ans = []
        for value , frequency in memo.items():
            if frequency==max_occurence:
                ans.append(value)
        return ans
        
            
                
            
        
        
        