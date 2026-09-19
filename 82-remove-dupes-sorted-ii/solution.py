# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return

        
        dummy_head = ListNode()
        dummy_head.next = head


        prev = dummy_head

        if not head.next:
            return head

        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    something = curr.next.next
                    curr.next = something
                #now its just prev and curr
                something = curr.next
                prev.next = something
                curr = something

            else:
                prev = curr
                curr = curr.next

        return dummy_head.next



'''
idea here is to use prev and curr
for each curr, check if curr.next == curr
while it is, remove curr.next
then at the end, remove curr as well

have to use a dummynode at the beginning for the case where the first node is a dupe
#also to keep track of what to return at the end

Time: O(n)
Space: O(1)


'''