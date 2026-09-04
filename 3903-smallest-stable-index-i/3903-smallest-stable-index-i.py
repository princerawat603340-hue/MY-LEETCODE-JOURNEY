class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        instability_score=0
        if len(nums)==1:
            return 0
        for i in range(len(nums)):
            instability_score=max(nums[:i+1])-min(nums[i:])
            if instability_score<=k:
                return i
        return -1
        