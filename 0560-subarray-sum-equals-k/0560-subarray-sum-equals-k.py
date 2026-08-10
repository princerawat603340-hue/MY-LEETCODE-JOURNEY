class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count