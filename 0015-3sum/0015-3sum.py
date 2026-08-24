class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        arr=[]
        s=set()
        if len(nums)<3:
            return arr
        else:
            for i in range(len(nums)-2):
                strt=i+1
                end=len(nums)-1
                while strt<end:
                    if nums[strt]+nums[end]==-(nums[i]):
                        s.add((nums[i],nums[strt],nums[end]))
                        end-=1
                    elif nums[strt]+nums[end]<-(nums[i]):
                        strt+=1
                    else:
                        end-=1
        for x in s:
            arr.append(list(x))
        return arr
