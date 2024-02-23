# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #  divide the tree to two part such as left and right
        left_tree_head = root.left
        right_tree_head = root.right
        def dfs(left_tree, right_tree):
            # if both reached the last equelly then we have same tree untill that point or 
            #  should return True
            if not left_tree and not right_tree:
                return True
            # in other case we have about 3 condition
            #  left_tree reached none before the right
            #  right_tree reached none before the left
            #  reached node that is not none but have value that are unequal
            condition_one = not left_tree and right_tree
            condition_two = not right_tree and left_tree
            if condition_one or condition_two or right_tree.val!=left_tree.val:
                return False
            return dfs(left_tree.left,right_tree.right) and dfs(left_tree.right, right_tree.left)
        return dfs(left_tree_head, right_tree_head)

        