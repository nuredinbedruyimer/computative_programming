# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        index=-1
        ans=[]
        stack=[]
        while head:
            index=index+1
            ans.append(0)
            while stack and stack[-1][1]<head.val:
                curIndex,value=stack.pop()
                ans[curIndex]=head.val
            stack.append((index,head.val))
            head=head.next
        return ans
        