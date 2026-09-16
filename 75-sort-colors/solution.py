class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, len(nums) - 1

        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1

            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            
            else:
                i += 1


'''
the idea here is to separate the in place array into 4 sections
zero | ones | unknown | twos
use a pointer for left and right (where to places 0's and 2's)
when you find a zero, swap with l pointer and then increase l and i
when you find a two, swap with r pointer and then decrease r
BUT: dont increase i yet because need to check the new i value
#else (1 case) simply just move up i

Time: O(n)
Space: O(1)
'''