def inorder(root, ans):
    if not root:
        return 

    inorder(root.left, ans)

    ans.append(root.val)

    inorder(root.right, ans)

def build_bst_from_sorted_list(arr, left, right):
    if left>right:
        return None
    middle = (left+right)//2
    node = TreeNode(arr[middle])
    node.right = build_bst_from_sorted_list(arr, middle+1,right )
    node.left = build_bst_from_sorted_list(arr, left,middle-1 )
    return node



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        #  accessing sorted values from the bst using inorder traversal
        arr  = []

        inorder(root, arr)

        #  build the bst using sorted list we get from the inordr traversal value
        left = 0

        right = len(arr)-1 

        return build_bst_from_sorted_list(arr, left, right)


        