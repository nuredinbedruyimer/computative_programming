class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        counter=0
        axCounter=0
        for i in range(k):
            if s[i] in vowels:
                counter+=1
        left=0
        
        maxCounter=counter
        
        for j in range(k,len(s)):
            if(s[left]) in vowels:
                counter=counter-1
            left=left+1
            
                
            if s[j] in vowels:
                counter=counter+1
                
            maxCounter=max(maxCounter,counter)
        return maxCounter
            
            
        