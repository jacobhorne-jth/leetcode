class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        going_down = False
        curr = 0

        for ch in s:
            rows[curr].append(ch)

            if curr == 0 or curr == numRows - 1:
                going_down = not going_down


            if going_down:
                curr += 1

            else:
                curr -= 1

        
        return "".join(["".join(row) for row in rows])


#basic idea is just to create that zig zag pattern using a going down variable and a current row indicator
#and then a list of lists to simulate each row
#and then at the end join them

#remember the edge cases of if numRows == 1 or if numRows >= len(s) cause then just return s

#Time: O(n)
#Space: O(n)