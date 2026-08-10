class Solution(object):
    def noofhours(self, piles, speed) :
        sum=0
        for i in range(len(piles)) :
            if piles[i]%speed!=0:
                sum+=(piles[i]//speed) +1
            else:
                sum+=(piles[i]//speed)
        return sum
            

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        strt= 1
        end=max(piles)
        while strt <=end:
            mid=(end+strt)//2
            if self.noofhours(piles,mid)>h:
                strt=mid+1
            elif self.noofhours(piles, mid) <=h:
                end=mid-1
            
        return strt
                
