class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        result=s+s
        return goal in result and len(goal)*2==len(result)