def get_left(arr, target):

    low = -1

    high = len(arr)

    while high > low + 1 :

        middle = low + (high - low) // 2

        if arr[middle] > target:
            high = middle
        else:
            low = middle
    
    return low



test = int(input())

arr = list(map(int, input().split()))

arr.sort()

queries = int(input())

for _ in range(queries):
    curr = int(input())

    print(get_left(arr, curr)+1)
