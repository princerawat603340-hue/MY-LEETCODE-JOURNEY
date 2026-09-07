class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=1
        ans=''
        i=1
        while i<len(s):
            
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


     