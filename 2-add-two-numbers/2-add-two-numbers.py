# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        adder=ListNode(val=(l1.val+l2.val)%10)
        carry=(l1.val+l2.val)//10
        current_node=adder
        while l1.next and l2.next:
            l1=l1.next
            l2=l2.next
            current_node.next=ListNode(val=(carry+l1.val+l2.val)%10)
            carry=(carry+l1.val+l2.val)//10
            current_node=current_node.next
        while(l1.next):
            l1=l1.next
            current_node.next=ListNode(val=(carry+l1.val)%10)
            carry=(carry+l1.val)//10
            current_node=current_node.next
        while(l2.next):
            l2=l2.next
            current_node.next=ListNode(val=(carry+l2.val)%10)
            carry=(carry+l2.val)//10
            current_node=current_node.next
        if carry>0:
            current_node.next=ListNode(val=carry)
            
        return (adder)
            
