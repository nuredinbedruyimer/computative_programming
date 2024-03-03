def bfs(root):

    queue = deque([(root, 1)])
    ans = 0
    while queue:

        left_index = queue[0][1]
        right_index = queue[-1][1]
        ans = max(ans, right_index - left_index + 1)

        for _ in range(len(queue)):
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, index * 2))
            if node.right:
                queue.append((node.right, index * 2 + 1))

    return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return bfs(root)
            
