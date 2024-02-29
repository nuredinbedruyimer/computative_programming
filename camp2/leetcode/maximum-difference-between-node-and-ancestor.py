def dfs(root, largest, smallest):
    if not root:
        return largest-smallest
    smallest = min(smallest, root.val)
    largest = max(largest, root.val)
    left = dfs(root.left, largest, smallest)
    right = dfs(root.right, largest, smallest)
    return max(left, right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
       return dfs(root, 1, 100000+2)