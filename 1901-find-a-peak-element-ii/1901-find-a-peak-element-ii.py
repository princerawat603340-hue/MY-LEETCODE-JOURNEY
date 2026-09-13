class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        for x in mat:
            x.insert(0,-1)
            x.append(-1)
        mat.insert(0,[-1]*len(mat[0]))
        mat.append([-1]*len(mat[0]))
        for i in range(1,len(mat)-1):
            for j in range(1,len(mat[0])-1):
                if mat[i][j]>mat[i-1][j] and mat[i][j]>mat[i][j-1] and mat[i][j]>mat[i+1][j] and mat[i][j]>mat[i][j+1]:
                    return [i-1,j-1]