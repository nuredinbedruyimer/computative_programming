# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def get_answer():
            dummy=ListNode()
            sortingPointer=dummy
            listOnePointer=list1
            listTwoPointer=list2
            while listOnePointer and listTwoPointer:
                if listOnePointer.val<listTwoPointer.val:
                    sortingPointer.next=listOnePointer
                    listOnePointer=listOnePointer.next
                else:
                    sortingPointer.next=listTwoPointer
                    listTwoPointer=listTwoPointer.next
                sortingPointer=sortingPointer.next
            if listOnePointer:
                sortingPointer.next=listOnePointer
            elif listTwoPointer:
                sortingPointer.next=listTwoPointer
            return dummy.next
        return get_answer()