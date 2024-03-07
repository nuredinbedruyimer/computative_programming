def binary_search(citations):

    N = len(citations)

    low = 0

    high = N - 1

    ans = 0

    while low <= high:

        middle = ( low + high ) // 2

        if citations[middle] >= N - middle:

            ans = N - middle

            high = middle - 1

        else:

            low = middle + 1
    
    return  ans




class Solution:
    def hIndex(self, citations: List[int]) -> int:

        return binary_search(citations)