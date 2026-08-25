class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=set(nums)
        for i in range(1, len(nums)+2):
            if k*i not in s:
                return k*i
                