class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(val):
            #base cases:
            if val <= 2:
                return val

            #check memo
            if val in memo:
                return memo[val]

            memo[val] = helper(val - 1) + helper(val - 2)
            return memo[val]
        return helper(n)


#recursion with memory
#basically recurse as you would
#but store the sums per value
#calculate n stairs as the sum of n - 1 stairs and n - 2 stairs
#and keep doing that downwards
#storing [val]: distinct ways to climb n steps

#base case is 1 or 2 so val <= 2: return itself
#then check memo (whole point of this)

#otherwise, calculate it and store in memo
#helper(val - 1) + helper(val - 2) because of two options: 1 step away from n or 2
#return that new value

#Time: O(n) because only once per 1 -> n, otherwise dictionary lookip, would be more without dynamic programming
#Space: O(n) because memo should store once for each 1->n
