class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==1000:
                sum=1
            else:
                first_num=nums[i]//100
                second_num=(nums[i]//10)%10
                third_num=nums[i]%10
                sum=first_num+second_num+third_num
            if sum==i:
                return i
        return -1
        