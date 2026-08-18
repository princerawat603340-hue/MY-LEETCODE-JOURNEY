class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        rowst=0
        rowend=len(matrix)-1
        colst=0
        colend=len(matrix[0])-1

        while (rowst<=rowend) and (colst<=colend):
            for i in range(colst,colend+1):
                ans.append(matrix[rowst][i])
            rowst+=1
            for i in range(rowst,rowend+1):
                ans.append(matrix[i][colend])
            colend-=1
            if rowst<=rowend:
                for i in range(colend,colst-1,-1):
                    ans.append(matrix[rowend][i])
            rowend-=1
            if colst<=colend:
                for i in range(rowend,rowst-1,-1):
                    ans.append(matrix[i][colst])
            colst+=1
        return ans
            
            