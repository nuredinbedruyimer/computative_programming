def get_answer():
    N = int(input())
    arr = input()
    #  use dectionaty to store number of Good sub array so far
    #  intialize our memo with value of 1 that have zero length with zero sum
    #  that is empty subarray
    memo = {0 : 1}
    ans = 0
    curr_sum = 0
    # 1 1 0 1 1 ---> 
    """
    curr_sum-window =  0 we have zero on memo
    then add that havlue(1) on our answer 
    ans = 1
    memo[0] = 2
    we have diff of 0 now as well 
    ans = 3
    when i get 0 i should mak my memo zero and start doing again our counting
    
    
    """
    
    for i in range(N):
        curr_sum += int(arr[i])
        diff = curr_sum - i - 1
        if diff not in memo:
            memo[diff] = 0
        
        memo[diff] += 1
        ans += memo[diff] - 1
        
    print(ans)
test = int(input())
 
for _ in range(test):
    get_answer()