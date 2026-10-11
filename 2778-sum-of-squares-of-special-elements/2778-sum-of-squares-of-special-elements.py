class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        n=len(nums)
        for i in range(len(nums)):
            if n%(i+1)==0:
                sum+=(nums[i])**2
        return sum