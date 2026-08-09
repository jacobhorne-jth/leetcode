from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] += 1
        curr = 0
        count = 0
        for num in nums:
            curr += num
            count += sums[curr - k]
            sums[curr] += 1
        
        return count


#basically for this one, use prefix sum + hash
#counts the number of subarrays that are at a certain count
#that count will be curr running sum - k as for 
#curr is the sum of everything we have seen so far
#is there a subarray ending here whos sum is k?
#curr - k = count of that subarray
#do that for every num in nums

#use default dict for default values of 0


#Time: O(n) because goes through each num in nums
#Space: O(n) worst case cause n different sums
        