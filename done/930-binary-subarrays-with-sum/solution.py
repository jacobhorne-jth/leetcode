from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        sums = defaultdict(int)
        sums[0] += 1

        count = 0
        curr = 0
        for num in nums:
            curr += num
            count += sums[curr - goal]
            sums[curr] += 1

        return count



#same idea as subarray sum equals k
#Time: O(n), Space: O(n)

#another viable solution is a sliding window approach since the numbers aren't negative
#but the idea above is much better / easier for the solution



        
        