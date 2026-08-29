class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        sets=set(jewels)
        for x in stones:
            if x in sets:
                count+=1
        return count