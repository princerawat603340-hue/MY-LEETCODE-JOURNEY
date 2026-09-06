class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        ans=0
        ind=0
        for i in range(len(mat)):
            if sum(mat[i])>ans:
                ans=sum(mat[i])
                ind=i
        return [ind,ans]
