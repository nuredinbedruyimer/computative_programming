class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        output,h=0,[]
        c=Counter(tasks)
        for k,v in c.items():
            heapq.heappush(h,(-v,k))
        while h:
            i,temp=0,[]
            while i<=n:
                output=output+1
                if h:
                    num,key=heapq.heappop(h)
                    num=num+1
                    if num <0 :temp.append((num,key))
                if not h and not temp:break
                i+=1
            for k,v in temp:
                heapq.heappush(h,(k,v))
        return output
        