class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dick={}
        for x in nums:
            if x in dick:
                dick[x]+=1
            else:
                dick[x]=1
        n=int(len(nums)/3) 
        ans=[]
        for x in dick:
            if dick[x]>n:
                ans.append(x)
        return ans
            