class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dick={}
        for x in s:
            if x not in dick:
                dick[x]=1
            else :
                dick[x]+=1
        for x in t:
            if x not in dick:
                return False
            else :
                dick[x]-=1
        for x in dick:
            if dick[x]!=0:
                return False
        return True