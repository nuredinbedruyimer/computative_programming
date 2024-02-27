# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
    
        def zig_zag(root):
            stack= collections.deque()
            stack.append(root)
            ans = []
            left_right = True
            while stack:
                length = len(stack)
                level =[]
                
              
                
                for i in range(length):
                    curr = stack.popleft()
           

                    

                    
                    if curr:
                        level.append(curr.val)
                    
                        stack.append(curr.left)
                    
                        stack.append(curr.right)


                
                
                if left_right and level:
                    ans.append(level)
                elif stack and not left_right:
                    ans.append(level[::-1])



                left_right = not left_right
            return ans

        return zig_zag(node)
        
        