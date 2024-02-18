class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
    
        def get_answer(process_time, tasks):
            process_time.sort()
            ans = []
            tasks.sort()
            N = len(process_time)
            max_time = 0
            for i in range(N):
                time_taken  = tasks[4*i+3]+process_time[N - 1- i]
                max_time = max(max_time, time_taken)
            return  max_time
        return get_answer(processorTime, tasks)
                