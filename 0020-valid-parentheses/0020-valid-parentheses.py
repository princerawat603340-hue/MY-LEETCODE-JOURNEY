class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr=[]
        for x in s:
            if arr:
                if x ==')' and arr[-1]=='(':
                    arr.pop()
                elif x =='}' and arr[-1]=='{':
                    arr.pop()
                elif x==']' and arr[-1]=='[':
                    arr.pop()
                else:
                    arr.append(x)
            else:
                arr.append(x)
        return not arr 


        