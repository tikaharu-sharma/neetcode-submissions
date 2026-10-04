class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = set()
        column_zero = set()

        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    column_zero.add(j)
        
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in column_zero:
                    matrix[i][j] = 0
        
        
        