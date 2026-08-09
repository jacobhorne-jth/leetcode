class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i, val in enumerate(nums):
            need = target - val
            if need in track:
                return [i, track[need]]
            else:
                track[val] = i


#basically, iterate through the list, keep tracking of value -> index found at
#first calculate the need value: target - val
#and then check if that value is in the seen dict already, in which place its good
#otherwise just set the val -> index in the track for later checks

#time: O(n) as it iterates through nums once
#space: O(n) worst case, if not found til the very end. Or not at all? (not possible most likely)