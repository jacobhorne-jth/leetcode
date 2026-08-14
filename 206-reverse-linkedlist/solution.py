# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head = None

        while curr:
            next_node = curr.next
            #run the reversal now
            #set curr.next to new_head
            #then new_head to prev curr

            curr.next = new_head
            new_head = curr

            curr = next_node

        return new_head



#basically for this one, need to iterate through the list, adding to a new linkedlist while storing the head
#return the head
#do this by having a new_head pointer to stay at front of new list
#and curr pointer to iterate through old list
#for each value of curr
#store its next value
#set curr to the the next of curr
#so like  curr -> new_head
#and then set new_head = curr
#  cause now the node in curr is the new head
#so it goes new_head (from curr) -> rest of the list
#that way new_head stays in front and can be returned at end

#Time: O(n) because go through each node
#Space: O(1) because same variables for no matter what length