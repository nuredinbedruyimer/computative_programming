def get_size(node):
    curr = node
    size = 0
    while curr:
        size += 1
        curr = curr.next
    return size


def get_answer(head, k):
    """
    1 2 3 4 5 6 7 8 9 10
    if n is deivisible by  k it have same number of nod but it is not
    we have extra value (node) on the remaining part


    step 1 ---> finding size of linkedlist
    step 2 ---> finding number of node we should assign
    step 3 ---->

    """
    # get size of linkedlist

    size = get_size(head)

    #  finding common value

    common_node_length = size // k

    #  remaining part

    remaining_node_length = size % k

    #  making that spliting
    ans = []
    curr = head

    for i in range(k):
        # for smmaler part we add None at last point
        #  we only need to find node( head node ) with distance of splitted length

        if not curr:
            ans.append(None)
        else:
            ans.append(curr)
            temp = 0
            if remaining_node_length > 0:
                temp = common_node_length + 1
            else:
                temp = common_node_length

            remaining_node_length -= 1

            while temp > 1:
                curr = curr.next
                temp = temp - 1

            node = curr.next
            curr.next = None
            curr = node
    return ans


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        return get_answer(head, k)
