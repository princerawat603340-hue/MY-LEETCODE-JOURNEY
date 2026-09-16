class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        dick=dict()
        count=0
        for i in range(len(s)):
            dick[s[i]]=1
            for j in range(i+1,len(s)):
                if s[j] not in dick:
                    dick[s[j]]=1
                else:
                    dick[s[j]]+=1
                count+=max(dick.values())-min(dick.values())
            dick=dict()
        return count
        