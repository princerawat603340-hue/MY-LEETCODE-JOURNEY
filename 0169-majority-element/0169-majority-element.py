class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==current:
                count+=1
            else:
                count-=1
                if count==0:
                    current=nums[i]
                    count=1
        return current