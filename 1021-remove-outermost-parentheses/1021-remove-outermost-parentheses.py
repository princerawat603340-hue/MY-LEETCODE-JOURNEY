class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=1
        ans=''
        j=0
        i=0
        while i<len(s):
            if i!=j:
                if s[i]=='(':
                    count+=1
                elif s[i]==')':
                    count-=1
                if count!=0:
                    ans+=s[i]
                else:
                    i+=1
                    count=1
            i+=1
                    
    


        return ans


     