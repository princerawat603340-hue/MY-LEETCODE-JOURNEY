class Solution(object):
    def merge(self,nums,l,m,r):
        i=l
        j=m+1
        temp=[]
        count=0

        for a in range(l, m + 1):
            while j <= r and nums[a] > 2 * nums[j]:
                j += 1

            count += j - (m + 1)
        j=m+1
        
        while i<=m and j<=r:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i+=1
            else:
                temp.append(nums[j])
                j+=1
        while i<=m:
            temp.append(nums[i])
            i+=1
        while j<=r:
            temp.append(nums[j])
            j+=1
        nums[l:r+1]=temp
        return count


    def mergesort(self,nums,strt,end):
        if strt>=end:
            return 0
        mid=(strt+end)//2
        leftcount=self.mergesort(nums,strt,mid)
        rightcount=self.mergesort(nums,mid+1,end)
        count= self.merge(nums,strt,mid,end)
        return count+leftcount+rightcount
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        strt=0
        end=len(nums)-1
        count=self.mergesort(nums,strt,end)
        return count
        