# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyNode = ListNode(0)
        curr = dummyNode

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else: 
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummyNode.next


#idea for this is just to store a carry var
#and the l1 and l2 value
#while any one of them exists, keep going
#keep a dummyhead at head of new one tho
#at each step, set val1 to l1.val if it exists, and 0 otherwise
#same for l2

'''
Calculate total
caculate carry and digit using // 10 and % 10 respectively
then remember to set them to the next
'''

#The way at each one, you sum that up l1 val + l2 val + carry (l1 and l2 vals are 0 if the node doesnt exist)

#Time: O(max(l1, l2))
#Space: O(1)