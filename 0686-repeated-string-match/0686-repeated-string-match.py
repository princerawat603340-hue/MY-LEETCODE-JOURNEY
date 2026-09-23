class Solution(object):
    def repeatedStringMatch(self, a, b):
        count = len(b)//len(a)

        s = a * count

        if b in s:
            return count

        if b in s + a:
            return count + 1
        if b in s+2*a:
            return count+2

        return -1