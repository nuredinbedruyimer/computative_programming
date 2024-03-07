from bisect import bisect_left


def binary_search(arr, target):

    low = 0

    high = len(arr) - 1

    ans = -1

    while low <= high:

        middle = ( low + high ) // 2

        if arr[middle][0] == target:

            return arr[middle][1]
        
        elif arr[middle][0] > target :

            ans = arr[middle][1]

            high = middle - 1
        
        else:

            low = middle + 1

    return ans




def get_sorted_start(intervals):

    N = len(intervals)

    start = []

    for i in range(N):

        start.append((intervals[i][0], i))

    start.sort(key = lambda x : x[0])

    return start

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        N = len(intervals)

        sorted_start = get_sorted_start(intervals)

        ans = [-1 for _ in range(N)]


        for i in range(N):

            index = binary_search(sorted_start, intervals[i][1])

            
            ans[i] = index

        return ans


            
            

        