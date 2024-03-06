def get_answer(arr, K):

    N = len(arr)

    prefix_sum = [0 for _ in range(N+1)]

    for i in range(N):

        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    
    queue = deque()

    INF = float('inf')
    
    ans_window = INF

    curr_sum = 0


    for i in range(N + 1):

        

        
        while queue and prefix_sum[i] - prefix_sum[queue[0]] >= K:

            ans_window = min(ans_window, (i - queue.popleft()))
        
        while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:

            queue.pop()
        
        queue.append(i)
    
    return ans_window if ans_window != INF else -1
        







class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        return get_answer(nums, k)
        
                
                
        