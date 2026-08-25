class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        string=strs[0]
        ans=''
        flag=0
        length=min(len(x) for x in strs)
        if len(strs)==1:
            return strs[0]
        for i in range(length):
            char=strs[0][i]
            for j in range(len(strs)):
                if strs[j][i]!=char:
                    flag=1
            if flag==0:
                ans+=char
            else:
                break
        return ans

                