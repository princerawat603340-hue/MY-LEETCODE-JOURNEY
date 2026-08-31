class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dick={}
        ans1=1
        for i in range(len(s)):
            if s[i] not in dick:
                dick[s[i]]=t[i]
            else:
                if dick[s[i]]!=t[i]:
                    ans1=0
        
        dick2={}
        ans2=1
        for i in range(len(t)):
            if t[i] not in dick2:
                dick2[t[i]]=s[i]
            else:
                if dick2[t[i]]!=s[i]:
                    ans2=0
                    
        
    
        return ans1==ans2 and ans1==1
                    
        