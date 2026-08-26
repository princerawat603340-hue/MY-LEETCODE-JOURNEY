class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans=[]
        
        
        for i in range(len(s)):
            string=''
            count=0
            if s[i]=='1':
                count+=1
            string+=s[i]
            if count==k:
                ans.append(string)
            for j in range(i+1,len(s)):
                if s[j]=='1':
                    count+=1
                    if count==k:
                        string+=s[j]
                        ans.append(string)
                        break
                string+=s[j]
        if not ans:return ''
        min_len = min(map(len,ans))
        arr=[x for x in ans if len(x)==min_len]
        return min(arr)




