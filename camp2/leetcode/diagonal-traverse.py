class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        ans = []
        1  2  3
        4  5  6
        7  8  9
        start from (0, 0) and direction to that of up-right
        then i get 1 and add to ans
        then my ans become ans = [1] becuse we finished traversing in up-right
        side i must move to other direction
        direction now become down-left and start from (0, 1)-- to move to the left 
        part the only thing i can do is updating the row
        we have like (0,1), (1,0) ---> values  his is done by move down rowise and
        left columnwise
        get value (2,4)
        then my become ans = [1, 2,4]
        because i reach j==0 i shold change direction to up and right
        and get value by moving up rowise(row-1) right columnwise(col+1)
        and my ans become ans [1, 2, 4,7,5,3......]


        NB ---> the only thing i want is traversing  Row*Col time over the matrix and do the thing only on the index

        
        
        """
        def get_answer():
            N = len(mat)
            M = len(mat[0])
            ans =[]
            memo= defaultdict(list)
            for row in range(N):
                for col in range(M):
                    memo[row+col].append(mat[row][col])
            for key in sorted(memo.keys()):
                if key%2:
                    ans.extend(memo[key])
                else:
                    ans.extend(memo[key][::-1])
            
 
            return ans
        return get_answer()
                    


                

            
        