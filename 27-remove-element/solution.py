class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        r = len(nums) - 1
        l = 0

        while l <= r:
            if nums[l] == val:
                nums[r], nums[l] = nums[l], nums[r]
                count += 1
                r -= 1

            else:
                l += 1

            
        return len(nums) - count


#this one is pretty simple
#use the similar idea to sort colors
#have a pointer to iterate through the list
#and a pointer at the end 
#when you find a val
#swap with that end pointer and decrease it
#working zone | val zone
#then return the lenght of that working zone (the none val)
#for that, keep count of vals found then sub from len of nums

#Time: O(n)
#Space: O(1)