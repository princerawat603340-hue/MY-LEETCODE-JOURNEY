class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        maxi=0
        for x in s:
            if x=='(':
                count+=1
            elif x==")":
                maxi=max(maxi,count)
                count-=1
        return maxi 