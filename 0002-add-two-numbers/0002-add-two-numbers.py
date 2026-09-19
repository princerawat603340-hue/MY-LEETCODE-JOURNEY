class Solution(object):
    def addTwoNumbers(self, l1, l2):

        head = l1
        carry = 0

        while l1 and l2:

            total = l1.val + l2.val + carry

            l1.val = total % 10
            carry = total // 10

            prev = l1

            l1 = l1.next
            l2 = l2.next
        if l2:
            prev.next = l2

            while l2:
                total = l2.val + carry

                l2.val = total % 10
                carry = total // 10

                prev = l2
                l2 = l2.next
        elif l1:
            while l1:
                total = l1.val + carry

                l1.val = total % 10
                carry = total // 10

                prev = l1
                l1 = l1.next
        if carry:
            prev.next = ListNode(carry)

        return head

