class Solution(object):
    def generate(self, numRows):
        ans = []

        arr = [1]
        ans.append(arr)

        if numRows == 1:
            return ans

        arr = [1, 1]
        ans.append(arr)

        while len(ans) != numRows:
            num = ans[-1]
            arr = [1]

            for i in range(len(num) - 1):
                arr.append(num[i] + num[i + 1])

            arr.append(1)
            ans.append(arr)

        return ans