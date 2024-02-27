# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def LCA(p, q):
            curr=root
            while curr:
                #  if both the curr decendant is greater than  the curr value
                #  i should move to the right and  finnd if the lca found on that dir
                if p.val>curr.val and q.val>curr.val:
                    curr=curr.right
                #  if both are less than the curr node i shold find them on other dirsection
                elif p.val<curr.val and q.val<curr.val:
                    curr=curr.left
                # else we find our LCA for the given node on curr node beacuse it is eithrt
                #  p.val>curr.val and q.val<curr.val or q.val<curr.val and q.val>curr.val
                
                else:
                    return curr
        return LCA(p, q)
        
        