class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=-1*nums[i]
        n=len(nums)
        nums.sort()
        sum=0
        i=0
        while i<n//2:
            sum-=(nums[i])*(nums[i])
            i+=1
        while i<n:
            sum+=(nums[i])*(nums[i])
            i+=1
        return sum
