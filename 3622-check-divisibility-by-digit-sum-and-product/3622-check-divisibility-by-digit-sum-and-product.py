class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum=0
        product=1
        temp=n
        while temp !=0:
            sum+=temp%10
            product*=temp%10
            temp=temp//10
        return n%(sum+product)==0
        