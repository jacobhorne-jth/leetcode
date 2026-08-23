class Solution:
    def rob(self, nums: List[int]) -> int:
        #at each house, need to know 
        #100, 1, 2, 400

        dp = [0] * len(nums)
        #each dp[i] should have the most possible at that index
        #and should be created by max(dp[i-1], dp[i-2] + n)

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        i = 2

        while i < len(nums):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            i += 1

        return dp[-1]



#use the fact that at each step, you ahve two options, rob or skp
#and what you do there s determned by what you dd in previous steps
#cause if you robbed the last one, you would have to skip

#need to ask what is the best answer for the problem up to here, and what smaller answers would let me build it
#use a dict (dp) to track the max u couldve reached at each i
#that amt is calculated by max of dp[i-1] and nums[i] + dp[i-2]
#f dp[i-1] is more, that means you would skip this house
#if dp[i-2] + nums[i] was more, you would rob ths house
#dp stores the best possble that can be achieved at that point, not what was actually done

#Tme: O(n)
#Space: O(n) 

#note: can have O(1) space by tracking using only two varables