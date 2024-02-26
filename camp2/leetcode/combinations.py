class Solution(object):
    def combine(self, n, k):
        # ans=[]
        # stack=[]
        # def combinations(start,k,stack):

        #     if len(stack)==k:
        #         ans.append(stack[:])
        #         return
    
        #     for i in range(start,n+1):
        #          stack.append(i)
        #          bt(i + 1,k,stack)
        #          stack.pop()
           
        # combinations(1,k,s)
        # return ans
        ans=[]
        stack=[]
        def combinations(start,k,stack):
            if  len(stack)==k:
                ans.append(stack[:])
                return 
            if start > n:
                return 
            stack.append(start)
            combinations(start+1,k,stack)
            stack.pop()
            combinations(start+1,k,stack)
        combinations(1,k,stack)
        return ans
