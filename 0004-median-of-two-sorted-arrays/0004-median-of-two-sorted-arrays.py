class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result=[]
        i=0
        j=0
        while i <len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
            else :
                result.append(nums2[j])
                j+=1
        while i <len(nums1):
            result.append(nums1[i])
            i+=1
        while j <len(nums2):
            result.append(nums2[j])
            j+=1
        n=len(result)
        if n%2==0:
            return (result[n//2]+ result[(n//2)-1])/2.0
        else:
            return result[n//2]