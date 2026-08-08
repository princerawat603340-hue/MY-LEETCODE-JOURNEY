class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                rep=nums[i]
                nums[i]=nums[j]
                nums[j]=rep

                i+=1
        