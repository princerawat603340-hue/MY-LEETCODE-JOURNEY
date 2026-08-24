class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        temp=num
        while temp!=0:
            if temp%2==0:
                temp=temp/2
                count+=1
            else:
                temp=temp-1
                count+=1
        return count
            