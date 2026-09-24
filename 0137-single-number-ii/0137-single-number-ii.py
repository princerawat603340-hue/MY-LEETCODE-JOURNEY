class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset=dict()
        for x in nums:
            if x not in hashset:
                hashset[x]=1
            else:
                hashset[x]+=1
        for key in hashset:
            if hashset[key]==1:
                return key