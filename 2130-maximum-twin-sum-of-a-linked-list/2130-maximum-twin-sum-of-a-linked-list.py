# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        current=head
        while current is not None:
            arr.append(current.val)
            current=current.next
        maxTwin=0
        length=len(arr)
        for i in range(length):
            maxTwin=max(maxTwin,arr[i]+arr[length-i-1])
        return maxTwin
            
        