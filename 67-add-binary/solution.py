class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []

        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))

            carry = total // 2

        return "".join(reversed(result))


'''
ok for this one the key is understanding that
binary addition works the same except
0 + 0 = 0 with no carry
0 + 1 and 1 + 0 = 1 with no carry
1 + 1 = 0 with 1 carry

use this to add them iterating from right to left
add that total to a list
and then reverse that list

Time: O(max(N, M) where n and m are the lengths of the two strings
Space: O(max(N, M) same because the output string will be this or at most one more than that for times when the carry goes one over
'''