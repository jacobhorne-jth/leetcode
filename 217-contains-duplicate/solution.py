class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        return False

#set() creation = O(1), lookup (in operator) = O(1)
#basically just iterate through nums, if a value has been seen before (in seen set, return True, because contains dupe)
#if not add to set and continue, at the end, return False cause no dupes were found

#Time: O(n) worst case, if there are n unique numbers in nums
#Space: O(n) worst case, if there are n unique numbers in nums because they all get added to set
