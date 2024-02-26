# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def get_answer():
            
            dummy =ListNode(None)
            dummy.next = head
            prev = dummy
            curr = dummy.next

            i = 1
            while i<=left-1:
                curr = curr.next
                prev = prev.next
                i+=1
                
            #  start reversing the part
            
            for _ in range(right-left):
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next= temp
           

            return dummy.next
                

            
            
        return get_answer()

