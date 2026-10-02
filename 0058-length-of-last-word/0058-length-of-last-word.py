class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        i=len(s)-1
        count=0
        while i>=0:
            if s[i]==' ':
                break
            count+=1
            i-=1
        return count