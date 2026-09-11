class Solution:
    def totalNumbers(self, digits):
        ans = set()

        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue

                    if digits[i] == 0:       # leading zero
                        continue

                    if digits[k] % 2 != 0:   # last digit must be even
                        continue

                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(num)

        return len(ans)

        
        