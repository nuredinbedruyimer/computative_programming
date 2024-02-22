# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        forward = []
        temp = head

        while temp:
            forward.append(temp.val)
            temp = temp.next
        def get_reverse_list(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        reverse_head = get_reverse_list(head)
        backward = []

        
        while reverse_head:
            backward.append(reverse_head.val)
            reverse_head = reverse_head.next
        return backward==forward




        