class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix)

        for i in range(row//2):
            matrix[i], matrix[row-i-1] = matrix[row-i-1], matrix[i]
        
        for i in range(row):
            for j in range(i+1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        