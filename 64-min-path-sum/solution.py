class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue

                #now need to calculate top and left
                #at each spot, calcilate the one above and the one to the left
                #add the minmumum

                top = grid[r-1][c] if r > 0 else float('inf')
                left = grid[r][c-1] if c > 0 else float('inf')

                grid[r][c] += min(top, left)

        return grid[rows-1][cols-1]

'''
The way u solve this is think about it kind of backwards
start at each point
set it to the minimum of the previous top and left ones
except that wont work for the [0][0] part
so then for each r and c that isnt [0][0]
calcualte the above value and the left value (if r and c are greater than 0)
and then add the minimum of them to the current grid[r][c] so that it takes the minimum of the previous two paths

Time: O(m*n) to go throgh every single eleemtn
Space: O(1) cause only constant variables


'''