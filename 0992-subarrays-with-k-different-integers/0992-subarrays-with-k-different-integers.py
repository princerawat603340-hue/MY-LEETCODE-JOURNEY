class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def atmostk(k,nums):
            left=0
            dick=dict()
            count=0
            for right in range(len(nums)):
                dick[nums[right]]=1 if nums[right] not in dick else dick[nums[right]]+1
                while len(dick)>k:
                    dick[nums[left]]-=1
                    if dick[nums[left]]==0:
                        del dick[nums[left]]
                    left+=1
                count+=right-left+1
            
            return count
        return atmostk(k,nums)-atmostk(k-1,nums)

