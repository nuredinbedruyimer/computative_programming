class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
        
        
class MyLinkedList:
    

    def __init__(self):
        self.left=ListNode(0)
        self.right=ListNode(0)
        self.left.next=self.right
        self.right.prev=self.left
        
        

    def get(self, index: int) -> int:
        currentNode=self.left.next
        while currentNode and index>0:
            currentNode=currentNode.next
            index=index-1
        if currentNode and index==0 and currentNode!=self.right:
            return currentNode.val
        return -1
    
            
    def addAtHead(self, val: int) -> None:
        newNode, next ,prev=ListNode(val),self.left.next,self.left
        prev.next=newNode
        next.prev=newNode
        newNode.next=next
        newNode.prev=prev
        
        

    def addAtTail(self, val: int) -> None:
        newNode, next ,prev=ListNode(val),self.right,self.right.prev
        prev.next=newNode
        next.prev=newNode
        newNode.next=next
        newNode.prev=prev
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        current=self.left.next
        while current and index>0:
            current=current.next
            index=index-1
        if current and index==0:
            newNode, next ,prev=ListNode(val),current,current.prev
            prev.next=newNode
            next.prev=newNode
            newNode.next=next
            newNode.prev=prev
            
        
        

    def deleteAtIndex(self, index: int) -> None:
        current=self.left.next
        while current and index>0:
            current=current.next
            index=index-1
        if current and current!=self.right and index==0:
            next,prev=current.next,current.prev
            prev.next=next
            next.prev=prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)