# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left>right:
                return None
            middle = (left+right)//2
            value = nums[middle]
            root = TreeNode(value)
            root.left = dfs(left,middle-1)
            root.right = dfs(middle+1, right)
            
            return root
        return dfs(0, len(nums)-1)
            
        