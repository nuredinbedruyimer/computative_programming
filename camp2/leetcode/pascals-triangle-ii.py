class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # def get_row(row_number):
        #     ans = []
        #     element = 1
        #     ans.append(element)
        #     for i in range(rowIndex):
        #         element *= row_number-i
        #         element //=i+1
        #         ans.append(element)
        #     return ans
        # return get_row(rowIndex)
        ans = [1]
        def get_row(row_number, row):
            if row_number==0:
                return row
            curr_row = [1]
            for i in range(len(row)-1):
                curr_row.append(row[i]+row[i+1])
            curr_row = curr_row + [1]
            return get_row(row_number-1, curr_row)
        return get_row(rowIndex, ans)



        