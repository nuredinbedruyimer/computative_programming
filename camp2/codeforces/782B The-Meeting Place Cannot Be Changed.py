def get_south_largest(arr , speed , time):
    distances = []

    for i in range(len(arr)):
        distances.append((arr[i] + (speed[i] * time)))
    
    return min(distances)

def get_nort_largest(arr , speed , time):
    distances = []

    for i in range(len(arr)):
        distances.append((arr[i] - (speed[i] * time)))
    
    return max(distances)


def is_meeting_point(arr , speed, time):
    south_min = get_nort_largest(arr , speed , time)
    north_max = get_south_largest(arr , speed , time)

    return south_min <= north_max


def get_answer():

    N = int(input())

    positions = list(map(int, input().split()))

    speeds = list(map(int, input().split()))

    low = 0

    high =  1e9

    middle =  0

    e = 1e-7

    while abs(high - low) > e:

        middle = low +  (high - low) / 2

        if is_meeting_point(positions , speeds , middle):
            high = middle
        else:
            low = middle
    
    print(middle)


get_answer()







