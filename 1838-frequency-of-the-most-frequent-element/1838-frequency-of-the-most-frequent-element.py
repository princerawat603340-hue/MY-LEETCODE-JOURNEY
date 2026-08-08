class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        left = 0
        window_sum = 0
        answer = 0

        for right in range(len(nums)):

            window_sum += nums[right]

            while nums[right] * (right-left+1) - window_sum > k:
                window_sum -= nums[left]
                left += 1

            answer = max(answer, right-left+1)
        return answer