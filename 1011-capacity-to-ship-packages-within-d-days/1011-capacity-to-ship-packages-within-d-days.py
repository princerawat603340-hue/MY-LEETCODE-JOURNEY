class Solution(object):
    def noofdays(self,weights,mid):
        val=0
        sum=0
        for x in weights:
            sum+=x
            if sum>mid:
                val+=1
                sum=x
        val+=1
        return val
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            day=self.noofdays(weights,mid)
            if day<=days:
                high=mid-1
            else:
                low=mid+1
        return low
