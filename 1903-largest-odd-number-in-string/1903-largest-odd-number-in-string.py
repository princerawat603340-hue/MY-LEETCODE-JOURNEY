class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans=''
        sum=''
        for x in num:
            sum+=x
            if ord(x)%2!=0:
                ans=sum
        return ans
                
        