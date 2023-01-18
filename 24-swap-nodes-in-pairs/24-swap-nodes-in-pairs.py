# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        preNode=dummy
        currentNode=head
        while currentNode and currentNode.next:
            bigOfNextPair=currentNode.next.next
            endOfPrePair=currentNode.next
            endOfPrePair.next=currentNode
            currentNode.next=bigOfNextPair
            preNode.next=endOfPrePair
            preNode=currentNode
            currentNode=bigOfNextPair
        return dummy.next
        
       
        