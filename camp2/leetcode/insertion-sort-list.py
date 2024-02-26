# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_answer():
            arr = []
            curr=head
            
            while curr:

                arr.append(curr.val)
                curr = curr.next
            arr.sort()
            dummy = ListNode(None)
            sorted_head = dummy
            for i in arr:
                node = ListNode(i)
                dummy.next = node
                dummy = dummy.next
            return sorted_head.next
        return get_answer()
        