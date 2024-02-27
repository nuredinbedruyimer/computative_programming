class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        def get_answer():
            N = len(tickets)
            queue=deque([i for i in range(N)])
            ans_time=0
        
            while True:
                N = len(queue)
                for i in range(N):

                    now=queue.popleft()
                    tickets[now]-=1
                    if tickets[now]>=1:
                        queue.append(now)
                    
                    ans_time+=1
                    if tickets[k]==0:
                        return ans_time
                if not queue:
                    break
        return get_answer()
                
                
        