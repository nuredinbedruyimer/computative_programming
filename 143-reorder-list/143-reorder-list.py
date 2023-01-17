# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        preValue=slow.next=None
        while second:
            t=second.next
            second.next=preValue
            preValue=second
            
            second=t
        first,second=head,preValue
        while second:
            t1,t2=first.next,second.next
            first.next=second
            second.next=t1
            first,second=t1,t2
        
        