class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1]*n for _ in range(m)]
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1]

        ### above space complexity is O(n^2), we can do O(n)

        row = [1] * n

        for i in range(1, m):
            newRow = [1] * n
            for c in range(1,n):
                newRow[c] = newRow[c-1] + row[c]
            row = newRow
        
        return row[n-1]

