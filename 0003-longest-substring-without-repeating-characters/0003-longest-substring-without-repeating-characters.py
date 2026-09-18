class Solution(object):
    def yesorno(self,dick):
        for x in dick.values():
            if x==2:
                return False
        return True
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        dick=dict()
        count=0
        maxcount=0
        for right in range(len(s)):
            if s[right] not in dick:
                dick[s[right]]=1
                count+=1
            else:
                dick[s[right]]+=1
                maxcount=max(maxcount,count)
                while self.yesorno(dick) is False :
                    dick[s[left]]-=1
                    count-=1
                    if dick[s[left]]==0:
                        del dick[s[left]]
                    left+=1
                count+=1
        return max(maxcount,count)