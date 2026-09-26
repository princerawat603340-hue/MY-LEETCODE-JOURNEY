class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        ans=''
        i=0
        dick=dict()
        for x in knowledge:
            dick[x[0]]=x[1]
        while i<len(s):
            if s[i]=='(':
                pointer1=i
                while s[i] !=')':
                    i+=1
                if s[pointer1+1:i] in dick:
                    ans+=dick[s[pointer1+1:i]]
                else:
                    ans+='?'
            else:
                ans+=s[i]
            i=i+1
        return ans
