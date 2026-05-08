class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        curr_row = 0
        while curr_row < row:
            if target <= matrix[curr_row][col-1]:
                l, r = 0, col-1
                while l <= r:
                    m = (l+r) // 2
                    if matrix[curr_row][m] == target:
                        return True
                    elif matrix[curr_row][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                return False
            curr_row += 1
        return False