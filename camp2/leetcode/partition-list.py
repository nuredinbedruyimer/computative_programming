# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def get_answer():
            less_dummy = ListNode(0, None)
            less_head = less_dummy
            greater_dummy = ListNode(0, None)
            greater_head = greater_dummy
            curr = head
            is_found = False
            while curr:
               
                if curr.val<x:
                    node = ListNode(curr.val)
                    less_dummy.next = node
                    less_dummy = less_dummy.next
                
                else:
                    node = ListNode(curr.val)
                    greater_dummy.next = node
                    greater_dummy = greater_dummy.next


                curr=curr.next
            
             
            
            greater_head = greater_head.next
            

            less_dummy.next = greater_head
            return less_head.next

           
            






        return get_answer()
        