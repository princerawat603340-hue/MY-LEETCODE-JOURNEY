class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        for i in range(len(s)-1):
            if s[i]=="I" and s[i+1]!='V' and s[i+1]!='X':
                sum+=1
            elif  s[i]=="I" and (s[i+1]=='V' or  s[i+1]=='X') :
                sum-=1
            if s[i]=='V':
                sum+=5
            if s[i]=="X" and s[i+1]!='L' and s[i+1]!='C':
                sum+=10
            elif s[i]=="X" and (s[i+1]=='L' or s[i+1]=='C'):
                sum-=10
            if s[i]=="L":
                sum+=50
            if s[i]=='C' and s[i+1]!='D' and s[i+1]!='M':
                sum+=100
            if s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'):
                sum-=100
            if s[i]=='D':
                sum+=500
            if s[i]=='M':
                sum+=1000

        if s[-1]=="I":
            sum+=1
        if s[-1]=="V":
            sum+=5
        if s[-1]=="X":
            sum+=10
        if s[-1]=="L":
            sum+=50
        if s[-1]=="C":
            sum+=100
        if s[-1]=="D":
            sum+=500
        if s[-1]=="M":
            sum+=1000
        return sum
            
