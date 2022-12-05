# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        x=None
        while slow:
            temp=slow.next
            slow.next=x
            x=slow
            slow=temp
        l,r=head,x
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
            
        