class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right=0
        left=0
        for i in range(len(nums)):
            right+=nums[i]
        for i in range(len(nums)):
            right-=nums[i]
            if right==left : return i
            left+=nums[i]
        return -1