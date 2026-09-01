class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr=s.split()
        ans=''
        for i in range(len(arr)-1,-1,-1):
            ans+=arr[i]+' '
        return ans[0:-1]



