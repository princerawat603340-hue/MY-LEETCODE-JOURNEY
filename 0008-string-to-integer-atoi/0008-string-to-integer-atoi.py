class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=''
        sign=1
        s=s.strip()
        if not s:
            return 0
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                sign=-1
            for i in range(1,len(s)):
                if s[i].isdigit():
                    ans+=s[i]
                else:
                    break
            
        else :
            for x in s:
                if x.isdigit():
                    ans+=x
                else:
                    break
         
        if not ans:
            return 0
        sum=0
        for i in range(len(ans)):
            sum+=int(ans[i])*10**(len(ans)-i-1) 
        if sum > ((2**31)-1):
            if sign==-1:
                sum=(2**31)
            else :
                sum=(2**31)-1
        return sum*sign