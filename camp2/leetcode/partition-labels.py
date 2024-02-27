class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def get_answer():
            last_index_memo={}
            N = len(s)
            start=0
            end=0
            ans=[]
            for i in range(N):
                last_index_memo[s[i]]=i
            for i in range(N):
                end=max(end,last_index_memo[s[i]])
                start=start+1
                if i==end:
                    ans.append(start)
                    start=0
            return ans
        return get_answer()

        
        