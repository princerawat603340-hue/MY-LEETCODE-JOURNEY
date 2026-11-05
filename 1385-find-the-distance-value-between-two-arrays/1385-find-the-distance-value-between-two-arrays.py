class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count=0
        flag=True
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if arr1[i]-arr2[j]<0 and arr2[j]-arr1[i]<=d:
                    flag=False
                elif arr1[i]-arr2[j]>=0 and arr1[i]-arr2[j]<=d :
                    flag=False

            if flag is True:
                count+=1
            else:
                flag=True
        return count
            

                 
        