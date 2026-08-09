class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff=[0]*(n+1)
        for first,last,seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats
        ans=[]
        total=0
        for i in range(n):
            total+=diff[i]
            ans.append(total)
        return ans
