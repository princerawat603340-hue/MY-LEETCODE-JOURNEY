class Solution(object):
    def countvalue(self,mid, nums):
        count=1
        sum=0
        for x in nums:
            if sum+x>mid:
                count+=1
                sum=x
            else :
                sum+=x
        return count
            
        
        
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low=max(nums)
        high =sum(nums)
        
        while low<=high:
            mid=(low+high)//2
            if self.countvalue(mid, nums)>k:
                low=mid+1
            else:
                high=mid-1
        return low