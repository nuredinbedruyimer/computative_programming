# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next  :
            return False
        def get_answer():
            slow = head 
            fast = head.next
            while fast.next and fast.next.next:
                if slow==fast:
                    return True
                slow = slow.next
                fast = fast.next.next
            return False
        return get_answer()
        