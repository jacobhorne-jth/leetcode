class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #subarray means cant sort

        #find the max subarray
        #find the min subarray

        #return the max of max subarray and total sum - min subarray

        max_sum = nums[0]
        curr_sum = nums[0]

        for n in nums[1:]:
            curr_sum = max(curr_sum + n, n)
            max_sum = max(max_sum, curr_sum)

        min_sum = nums[0]
        curr_sum = nums[0]

        for n in nums[1:]:
            curr_sum = min(curr_sum + n, n)
            min_sum = min(min_sum, curr_sum)

        if max_sum < 0:
            return max_sum

        return max(max_sum, sum(nums) - min_sum)

        
#for this one, main part is understanding how a max subarray works in a circular array
'''
two possibilities
one: the max subarray is just the normal one, can be solved without thinking about circular part
two: the wrap around is part of it in which case = the wrap around - the min subarray as if you are subtracting a contiguous part in the middle
you want that to be minizmied so the wrap around can be maximized

basically just find the max subarray sum and the min

and then return the max of max subarray sum and total sum - min subarray sum


use kadanes algo which basically u just iterate through list
store curr_sum and max/min sum
each step, update curr_sum so that it either continues: curr_sum + n, or starts over: n
and then also update max or min sum as the max or min of previously seen or currently seeing


Time: O(2n) = O(n) because two linear passes
Space: O(1) 

'''