class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        #can always remove the first or the last element
        #instead of going back and forth choosing which of the front
        #and the back to remove
        # you can instead find the longest continuous subarray that equals to
        #sum of the list - x

        total = sum(nums)
        target = total - x

        longest = -1

        if target < 0:
            #not possible
            return -1

        l = 0
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr > target and l <= r:
                curr -= nums[l]
                l += 1

            if curr == target:
                longest = max(longest, r - l + 1)
                
            

        if longest == -1:
            return -1

        return len(nums) - longest



#basically the approach here is to find the longest continuous subarray that equals to sum - x
#this is because that subarray = the subarray that exists after preforming the answer
#for minimum operations to substract x == 0
#and if longest is never updated means no subarrays found = -1 bc impossible

#first step is find lognest
#do that by iterating through r, keeping an L, increasing l (shrinking the window) when curr > target
#if they are equal, compare to longest

#at the end, return len(nums) - longest because thats how many operations that have to be done


#Time Complexity: O(n) because you iterate through nums once for sum and once for r to find the longest subarray
#Space: O(1) because no extra stuff