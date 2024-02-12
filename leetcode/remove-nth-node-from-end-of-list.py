# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        def get_length():
            length = 0
            curr = head
            while curr:
                curr = curr.next
                length+=1
            return length
        def get_answer():
            length = get_length()
            length =length-n
            
            prev=dummy = ListNode(0, head)
            
            for _ in range(length):
                prev=prev.next
            prev.next = prev.next.next
           
            return dummy.next
        return get_answer()
            
            