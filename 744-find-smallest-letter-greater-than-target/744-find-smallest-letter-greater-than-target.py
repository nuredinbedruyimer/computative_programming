class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left=0
        right=len(letters)-1
        flag=False
        while left<=right:
            middle=(left+right)//2
            
            if letters[middle]>target:
                right=middle-1
            else:
                left=middle+1
                flag=True

    
        return letters[left%len(letters)]












        