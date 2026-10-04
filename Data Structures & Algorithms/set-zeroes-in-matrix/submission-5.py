class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col0 = False #whether column 0 should be zeroed
        row, col = len(matrix), len(matrix[0])
        
        for i in range(row):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(row-1, -1, -1):
            for j in range(col-1, 0, -1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j] = 0
        if col0:
            for i in range(row):
                matrix[i][0] = 0
        
        


                
                


        
        
        