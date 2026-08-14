# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        res_head = ListNode()
        curr = res_head

        one = list1
        two = list2

        while one and two:
            if one.val > two.val:
                #add two
                curr.next = two
                two = two.next
                curr = curr.next
            else:
                #add one

                curr.next = one
                one = one.next
                curr = curr.next

        #now one or two

        while one:
            curr.next = one
            one = one.next
            curr = curr.next

        while two:
            curr.next = two
            two = two.next
            curr = curr.next

        return res_head.next



#for this one, walk through both linkedlists with pointers
#have a dummy head and a curr for the new linkedlist
#add the one who's value is less (so its sorted)
#while one and two

#once that loop is done, either list1 or list2 will still have elements

#have to handle that with while one:
#same logic of setting curr and then moving curr and one up

#same for two
#then remember to return dummy node . next for the head of the newly sorted

#Time: O(n1 + n2) because has to go through each linkedlist
#Space: O(1) because variables constant space