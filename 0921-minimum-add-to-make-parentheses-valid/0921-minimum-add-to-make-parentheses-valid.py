class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        count=0
        for x in s:
            if not stack:
                stack.append(x)
                count+=1
            else:
                if stack[-1]=='(' and x ==')':
                    count-=1
                    stack.pop()
                else:
                    count+=1
                    stack.append(x)
        return count
