# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        carry=0
        ans=[]
        l1node=l1
        l2node=l2
        while (l1node is not None )and(l2node is not None) :
            ans.append(((l1node.val+l2node.val+carry)%10))
            carry=(l1node.val+l2node.val+carry)//10
           
            l1node=l1node.next
            l2node=l2node.next
            
        while l1node is not None:
            ans.append((l1node.val+carry)%10) 
            carry=(l1node.val+carry)//10
            
            l1node=l1node.next
        while l2node is not None:
            ans.append((l2node.val+carry)%10)
            carry=(l2node.val+carry)//10
            l2node=l2node.next
        if carry!=0:
            ans.append(carry)
            
        head=ListNode(ans[0])
        curr=head
        for i in range(1,len(ans)):
            curr.next=ListNode(ans[i]) 
            curr=curr.next
        
        return head
    
           
           