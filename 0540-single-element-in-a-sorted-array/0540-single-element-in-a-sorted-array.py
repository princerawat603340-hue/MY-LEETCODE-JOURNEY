class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        while low<high:
            mid=(high+low)//2
            if mid%2==0:
                if nums[mid]==nums[mid+1]:
                    low=mid+1
                elif nums[mid]==nums[mid-1]:
                    high=mid-1
                else:
                    return nums[mid]
            else:
                if nums[mid]==nums[mid-1]:
                    low=mid+1
                elif nums[mid]==nums[mid+1]:
                    high=mid-1
                else:
                    return nums[mid]
        return nums[low]
                
            