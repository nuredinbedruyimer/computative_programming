
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def get_answer():
            # fixed sliiding window
            K = len(s1)
            N = len(s2)
            memo_one = defaultdict(int)
            memo_two = defaultdict(int)
            if K>N:
                return False

            for i in range(K):
                memo_one[s1[i]]+=1
                memo_two[s2[i]]+=1
            if memo_one==memo_two:
                return True
            for i in range(K,N):
                memo_two[s2[i-K]]-=1
                if memo_two[s2[i-K]]==0:
                    del memo_two[s2[i-K]]

                memo_two[s2[i]]+=1
                if memo_one==memo_two:
                    return True
            return False
        return get_answer()
                
                
       

        