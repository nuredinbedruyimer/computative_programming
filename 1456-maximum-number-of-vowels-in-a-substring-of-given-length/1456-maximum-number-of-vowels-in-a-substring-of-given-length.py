class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        counter=0
        maxCounter=0
        for left in range(k):
            if s[left] in vowels:
                counter+=1
       
        maxCounter=counter
        print(left)
        
        for right in range(k,len(s)):
            if(s[left-k+1]) in vowels:
                counter=counter-1
                
            left=left+1
            
                
            if s[right] in vowels:
                counter=counter+1
                
            maxCounter=max(maxCounter,counter)
        return maxCounter
            
            
        