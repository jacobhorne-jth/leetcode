from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = 0
        curr = 0
        for n in nums:
            if n % 2 != 0:
                curr += 1

            ans += counts[curr - k]
            counts[curr] += 1

        return ans


#for this problem, think of it as making each even value as 0 and odd as 1
#so now, each subarray with sum of k = a nice subarray
#counts stores the number of times we've seen a certain amount of odd values
#"how many times have i seen this number of odd numbers up until this point"

#and then curr will store the amount of odds we have seen up until this point
#but we dont want curr odds, we want curr - k because curr = k + ___ and you want to find how many times 
#you could cut it off to get k odds
#after doing that, add [curr] += 1 to reflect that we saw curr odds

#Time:O(n) because dict lookup = O(1) and go through nums once
#Space: O(n) because worst case, n + 1 different prefix counts