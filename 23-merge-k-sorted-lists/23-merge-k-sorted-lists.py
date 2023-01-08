# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 :
            return None
        while len(lists)>1:
            mList=[]
            for i in range(0,len(lists),2):
                lstOne=lists[i]
                lstTwo=lists[i+1] if i+1<len(lists) else None
                mList.append(self.merge(lstOne,lstTwo))
            lists=mList
        return lists[0]
    def merge(self,lstOne,lstTwo):
        dummy=ListNode() # head of linked list
        tail=dummy # in order to transvers over linked list element upto tail point
        while lstOne and lstTwo:
            if lstOne.val<lstTwo.val:
                tail.next=lstOne
                lstOne=lstOne.next
            else:
                tail.next=lstTwo
                lstTwo=lstTwo.next
            tail=tail.next
        if lstOne:
            tail.next=lstOne
        if lstTwo:
            tail.next=lstTwo
        
        return dummy.next
        
                    
                
            
        
        