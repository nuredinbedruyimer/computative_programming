class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def get_answer():
            A = 0
            B = 0
            N = len(bills)
            for i in range(N):
                if bills[i]==5:
                    A+=1
                elif bills[i]==10 and A>=1:
                    B+=1
                    A-=1
                elif bills[i]==20:
                    # min 15

                    
                    if B>=1 and A>=1:
                        B-=1
                        A-=1
                    elif A>=3:
                        A-=3
                    else:
                        return False
                else:
                    return False
            return True
        return get_answer()
            
            
        