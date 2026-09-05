class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = list(nums)
        left = list(nums)
        for x in range(1,len(nums)):
            right[x] = max(right[x],right[x-1])
        for x in range(len(nums)-2,-1,-1):
            left[x] = min(left[x],left[x+1])
        for x in range(len(nums)):
            score = right[x]-left[x]
            if score <= k:
                return x
        return -1