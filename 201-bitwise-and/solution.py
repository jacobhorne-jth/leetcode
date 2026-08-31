class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left != right:
            left >>= 1
            right >>= 1
            shifts += 1
        
        return left << shifts



#shift right: 1001 -> 100
#shift left: 1001 -> 10010


#can work by doing the ^= for every element but thats not needed
#can use the idea that all elements between left and right will have the same prefix until left and right no longer match
#once left and right no longer match: shift left back into place with all the 0's for the none matching ones
#do this by tracking how long until left == right
#once they are, shift left by that many elements

#Time: O(log right) where its right because left is guarenteed to be <= right
#its log right because its binary so each digit is a x2 or /2 shift

#Space: O(1) cause vars
