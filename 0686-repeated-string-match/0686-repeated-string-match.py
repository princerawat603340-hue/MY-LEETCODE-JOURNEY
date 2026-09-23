class Solution(object):
    def repeatedStringMatch(self, a, b):
        count = 1
        original = a

        while len(a) < len(b):
            a += original
            count += 1

        if b in a:
            return count

        a += original
        count += 1

        if b in a:
            return count

        return -1