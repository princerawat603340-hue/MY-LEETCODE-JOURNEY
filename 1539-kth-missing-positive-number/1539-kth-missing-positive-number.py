class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count=k
        for i in range(1, arr[-1]+k+2):
            if count==0:
                return i-1
            elif i not in arr:
                count-=1
    
            
            
    