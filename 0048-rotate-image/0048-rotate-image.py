class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                var=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=var
        for row in matrix:
            row.reverse()
        
            