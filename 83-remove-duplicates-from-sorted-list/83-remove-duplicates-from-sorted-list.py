# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        
        current=head
        # this is current node to tranverse on  the element of linked list
        
        while current:
            while (current.next and current.next.val==current.val):
                current.next=current.next.next
            current=current.next
        return dummy.next
        