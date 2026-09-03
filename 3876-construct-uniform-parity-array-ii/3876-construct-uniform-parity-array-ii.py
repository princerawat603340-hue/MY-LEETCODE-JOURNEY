class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        if min(nums1)%2!=0:
            return True
        else:
            for x in nums1:
                if x%2!=0:
                    return False
            return True
                    
            
                