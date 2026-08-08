class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count1=0
        count2=0
        count3=0
        for i in range(len(nums)):
            if nums[i]==0:
                count1+=1
            elif nums[i]==1:
                count2+=1
            else:
                count3+=1
        for i in range(count1):
            nums[i]=0
        for i in range(count2):
            nums[count1+i]=1
        for i in range(count3):
            nums[count1+count2+i]=2