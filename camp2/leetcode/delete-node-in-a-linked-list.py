# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        def delete_node():
            """
            just copy the next element to now node and delete the link of 
            node and the copied  node
            """


            # copy next node to node we given and chnage the val as next value
            #  and the next value also next of the next of deleted element
            next_node=node.next
            node.val=next_node.val
            node.next=next_node.next
        delete_node()
        