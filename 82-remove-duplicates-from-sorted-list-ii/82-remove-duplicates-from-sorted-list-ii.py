# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=slow=ListNode(0,head)
        while head:
            if head.next and head.next.val==head.val:
                while head.next and head.next.val==head.val:
                    head=head.next
                slow.next=head.next
            else:
                slow=slow.next
            head=head.next
        return dummy.next
            
            
                
            
       
               
            
            
        
        