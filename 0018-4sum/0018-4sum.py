class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        arr=[]
        s=set()
        nums.sort()
        if len(nums)<4:
            return arr
        else:
            for i in range(len(nums)-3):
                for j in range(i+1,len(nums)-2):
                    low=j+1
                    high=len(nums)-1
                    while low<high:
                        if nums[low]+nums[high]==(target-nums[i]-nums[j]):
                            s.add((nums[i],nums[j],nums[low],nums[high]))
                            low+=1
                            high-=1
                        elif nums[low]+nums[high]<(target-nums[i]-nums[j]):
                            low+=1
                        else:
                            high-=1
        for x in s:
            arr.append(list(x))
        return arr
             

        