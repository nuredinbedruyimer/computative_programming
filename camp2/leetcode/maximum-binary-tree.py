def get_max_index(arr):
    max_value = -1
    max_index =  -1
    N = len(arr)
    for i in range(N):
        if arr[i]>max_value:
            max_value = arr[i]
            max_index = i
    return max_index

def build_tree(arr):
    if not arr:
        return None
    index = get_max_index(arr)
    node = TreeNode(arr[index])
    node.right = build_tree(arr[index+1:])
    node.left = build_tree(arr[:index])
    return node



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        return build_tree(nums)



        """
        Time complexity -- > O(N*N)
        space complixity ===> O(N) from the stack
        
        
        """
        