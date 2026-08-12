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

        # approach prefix sum then in prefix if there
        #is an odd number then i will make combo with every even number behind it 
        #and same  with even no if there is an even number in prefix sum then all the odd no before it will make subarray of sum odd
                 
