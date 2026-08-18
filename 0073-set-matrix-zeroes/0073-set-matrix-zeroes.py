
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        column=[1]*len(matrix[0]) 
        row=[1]*len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=0
                    column[j]=0
        for i in range(len(column)):
            if column[i]==0:
                for j in range(len(matrix)):
                    matrix[j][i]=0
                    
        for j in range (len(row)):
            
            if row[j]==0:
                for i in range(len(matrix[0])):
                    matrix[j][i]=0
        