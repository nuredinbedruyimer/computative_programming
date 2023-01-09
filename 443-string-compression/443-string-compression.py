class Solution:
    def compress(self, chars: List[str]) -> int:
        counter=1
        left=0
        for right in range(1,len(chars)+1):
            if right<len(chars) and chars[right]==chars[right-1]:
                counter=counter+1
            else:
                chars[left]=chars[right-1]
                left=left+1
                if counter>1:
                    for i in str(counter):
                        chars[left]=i
                        left=left+1
                counter=1
        chars=chars[:left]
        return left
                    
                
            
        