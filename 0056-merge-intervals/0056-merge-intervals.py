class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            last = ans[-1]
            current = intervals[i]

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                ans.append(current)

        return ans