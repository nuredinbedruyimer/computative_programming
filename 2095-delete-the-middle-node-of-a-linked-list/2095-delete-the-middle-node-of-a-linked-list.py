# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        pointerBeforeSlow=head.next
        fast=head
        prev=dummy=ListNode(0,head)
        while fast and fast.next:
            prev=slow
            pointerBeforeSlow=pointerBeforeSlow.next
            
            slow=slow.next
            fast=fast.next.next
        prev.next=pointerBeforeSlow
        return dummy.next
        
        