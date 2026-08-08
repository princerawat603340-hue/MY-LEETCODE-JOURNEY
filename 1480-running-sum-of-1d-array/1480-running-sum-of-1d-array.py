class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        arr=[]
        for i in range(len(nums)):
            sum+=nums[i]
            arr.append(sum)
        return arr