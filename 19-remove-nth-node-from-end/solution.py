# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow, fast = dummy, dummy

        for i in range(n):
            fast = fast.next

        #now fast and slow are n apart
        #once fast = none, that means slow is at the one to remove

        #do fast.next so that u arent at fast/slow ur at fast.next/slow.next

        #then u can just skip the "slow" one
        while fast.next:
            fast = fast.next
            slow = slow.next

        #now fast is done
        slow.next = slow.next.next

        return dummy.next #for head



#THIS IS MOST OPTIMAL
#uses fast and slow pointer concept
#keep fast and slow n apart
#do this with a for loop: fast = fast.next

#use a dummy node before head, incase head is the one to change
#then while fast.next
#increase slow and fast
#once thats not true that means fast is the last one and slow is one before the one to remove
#cause n apart
#so that means slow.next should be set to slow.next.next
#and then return dummy.head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        
        if n > count:
            return
        
        remov = count - n

        counter = 0

        prev = ListNode()
        curr = head
        while curr:
            if remov == 0:
                head = head.next
                return head
            
            if counter == remov:
                prev.next = curr.next
                return head
            counter += 1
            prev = curr
            curr = curr.next


#this works by basically counting how many, figuring out which one to remove using count - n
#and then once its found, skipping it, returning head
#handles the edge case of it being the head by setting head to head.next and returning

#Time: O(2n) = O(n) because two passes
#Space; O(1)