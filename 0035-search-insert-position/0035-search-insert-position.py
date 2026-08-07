class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        strt=0
        end=len(nums)-1
        while strt<=end:
            mid=(strt+end)//2
            if nums[mid]<target:
                strt=mid +1
            elif nums[mid]>target:
                end=mid -1
            else:
                return mid
        return end+1

        

        