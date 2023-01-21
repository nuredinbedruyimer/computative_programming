# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        leftPointer=dummy
        rightPointer=head
        while rightPointer and n>0:
            rightPointer=rightPointer.next
            n=n-1
        while rightPointer:
            rightPointer=rightPointer.next
            leftPointer=leftPointer.next
        leftPointer.next=leftPointer.next.next
        return dummy.next