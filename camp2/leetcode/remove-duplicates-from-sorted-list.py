# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_answer():
            curr = head
            while curr:
                start = curr
                while curr and curr.next and curr.val==curr.next.val:
                    curr = curr.next
                curr = curr.next
                start.next = curr
            return head
        return get_answer()
                



        