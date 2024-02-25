# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr_sum, root):
            if not root:
                return 0
            curr_sum = curr_sum*10 + root.val
            if not root.right and not root.left:
                return curr_sum
            left = dfs(curr_sum,root.left)
            right = dfs(curr_sum,root.right)
            return left + right
        def get_answer():
            return dfs(0,root)
        return get_answer()
        