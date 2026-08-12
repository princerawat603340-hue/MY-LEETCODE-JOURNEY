class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        
        """
        sum=0
        count=0
        nums=[]
        for i in range(len(arr)):
            sum+=arr[i]
            nums.append(sum)
        odd=0
        even=1
        for i in range(len(nums)):
            if nums[i]%2==0:
                count+=odd
                even+=1
            else:
                count+=even
                odd+=1
        return count % (10**9 + 7)


                 