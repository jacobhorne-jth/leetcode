class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]

        for n in nums:
            if curr < 0:
                curr = 0

            curr += n
            max_sum = max(curr, max_sum)

        return max_sum
        

#use kadanes algo
#basically set max to the first element and keep a curr sub array sum
#for each n in nums
#if curr is negative, set it to 0 (starting a new subarray)
#then add new num to curr
#and set max to max of curr and previous max (to update it)

#Time: O(n)
#Space: O(1)