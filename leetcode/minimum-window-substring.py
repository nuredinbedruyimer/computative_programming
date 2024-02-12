from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        start left and right from left of string
        intialize out t counter
        
        
        '''
        if len(t)>len(s):
            return ''
        def minWindow(s,t):

            length=float('inf')
            span=[-1,-1]
            left=0
            ans=float('inf')
            counter_of_t=defaultdict(int)
            
            for x in t:
                counter_of_t[x]+=1
            t_length=len(counter_of_t)
            s_length=0
            counter_of_s=defaultdict(int)
            for right in range(len(s)):
                counter_of_s[s[right]]+=1
                if s[right] in counter_of_t and counter_of_s[s[right]]==counter_of_t[s[right]]:
                    s_length+=1
                while  t_length==s_length:
                    current_length=(right-left+1)
                    if current_length<ans:
                        span=[left,right]
                        ans=current_length
                        
                    counter_of_s[s[left]]-=1
                    if s[left] in counter_of_t  and counter_of_s[s[left]]<counter_of_t[s[left]]:
                        s_length-=1
                        
                    left=left+1
            return span
        left,right=minWindow(s,t)
        return ''.join(s[left:right+1]) 
                    
                    

                
                
            
            
        