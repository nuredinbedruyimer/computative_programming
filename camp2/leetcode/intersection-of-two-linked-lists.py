# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def find_intersection(startA, startB):
            one=startA
            two = startB
            while one!=two:
                one = one.next
                two = two.next
            return one


        curr_one = headA
        size_one = 0
        while curr_one:
            size_one+=1
            curr_one = curr_one.next
        curr_two =headB
        size_two = 0
        while curr_two:
            size_two+=1
            curr_two= curr_two.next
        temp_head = None

        if size_two >size_one:
            temp_head = headB
        else:
            temp_head = headA
        distance = abs(size_two-size_one)
        for _ in range(distance):
            temp_head = temp_head.next
        if size_two>size_one:
            return find_intersection(headA, temp_head)
        elif size_one>size_two:
            return find_intersection(temp_head , headB)
        else:
            return find_intersection(headA, headB)
