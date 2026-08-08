class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myset=set(nums)
        current=0
        length=0
        max_count=0
        for x in myset:
            if x-1 not in myset:
                current=x
                length=1
                while current + 1 in myset:
                    current=current+1
                    length=length+1
                max_count=max(max_count,length)
            
        return max_count

        