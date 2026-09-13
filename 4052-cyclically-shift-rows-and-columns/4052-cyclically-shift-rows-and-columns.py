class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        """
        :type n: int
        :type grid: List[List[int]]
        :type rowShift: List[int]
        :type colShift: List[int]
        :rtype: List[List[int]]
        """
        for i in range(len(rowShift)):
            row=[grid[i][j] for j in range(n)]
            for j in range(len(row)):
                grid[i][(j - rowShift[i] + n) % n]=row[j]
        for i in range(len(colShift)):
            col=[grid[j][i] for j in range(n)]

            for j in range(len(col)):
                grid[(j-colShift[i]+n)%n][i]=col[j]
        return grid