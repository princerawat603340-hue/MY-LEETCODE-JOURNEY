class Solution:
    def frequencySort(self, s: str) -> str:
        dick=dict()
        for x in s:
            if x not in dick:
                dick[x]=1
            else:
                dick[x]+=1
        dick=dict(sorted(dick.items(),key=lambda x : x[1],reverse=True))
        ans=''
        for x in dick:
            ans+=x*dick[x]
        return ans

        