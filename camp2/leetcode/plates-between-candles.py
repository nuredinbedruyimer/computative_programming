
def bisect_right(arr , target):
    low = 0
        
    high = len(arr)

    while low < high:
        
        mid = (low + high) // 2

        if target < arr[mid]:

            high = mid
        else:
            low = mid + 1
    return low


def bisect_left(arr , target):
    low = 0
        
    high = len(arr)

    while low < high:
        
        mid = (low + high) // 2

        if  arr[mid] < target:

            low = mid + 1
        else:
            high = mid

    return low


def get_plates(s):

    candle_position = []


    for i in range(len(s)):

        if s[i] == "|":

            candle_position.append(i)

    return candle_position





class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_position = [i for i, v in enumerate(s) if v == '|']

        ans = []
        for left,  right in queries:

            start = bisect_left(candle_position, left)

            end = bisect_right(candle_position, right)-1

            # print(start , end)

            if start < end:

                ans.append((candle_position[end] - candle_position[start]) - (end -start))

            else:

                ans.append(0)

        return ans