class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxstring=''
        for i in range(len(s)):
            low=i-1
            high=i+1
            while low>=0 and high<len(s):
                if s[low]==s[high]:
                    low-=1
                    high+=1
                else:
                    break
            string=s[low+1:high]
            if len(string)>len(maxstring):
                maxstring=string
            low=i-1
            high=i
            while low>=0 and high<len(s):
                if s[low]==s[high]:
                    low-=1
                    high+=1
                else:
                    break
            string=s[low+1:high]
            if len(string)>len(maxstring):
                maxstring=string
            

        return maxstring
                