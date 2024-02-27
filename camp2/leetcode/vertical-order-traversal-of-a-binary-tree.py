# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(root, distance_one, distance_two, memo):
            if not root:
                return 
            memo[(distance_one, distance_two,root.val)].append(root.val)
            left = dfs(root.left, distance_one+1,distance_two-1, memo)
            right = dfs(root.right, distance_one+1, distance_two+1, memo)
            
        memo = defaultdict(list)
        dfs(root, 0, 0, memo)
        print(memo)
        sorted_keys = sorted(memo.keys(),key=lambda x : (x[1], x[0],x[2]))
        memo_two = defaultdict(list)

        for v_distance , h_distance, value in sorted_keys:
            memo_two[h_distance].extend(memo[(v_distance, h_distance, value)])
        ans = []

        for i in memo_two:
            ans.append(memo_two[i])
        
        return ans
        