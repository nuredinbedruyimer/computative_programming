# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_answer():
            curr = head
           
            index = 1
            odd_dummy = ListNode(0, None)
            even_dummy = ListNode(0, None)

            odd_head = odd_dummy
            even_head = even_dummy
            while curr:
                if index % 2:

                    node = ListNode(curr.val)
                    odd_dummy.next = node
                    odd_dummy = odd_dummy.next

                else:
                    node = ListNode(curr.val)
                    even_dummy.next = node
                    even_dummy = even_dummy.next
                curr = curr.next
                index += 1

            odd_dummy.next = even_head.next
            return odd_head.next
        return get_answer()
