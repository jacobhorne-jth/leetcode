class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r,c+1) + dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    best = max(best, dfs(r, c))
    
            


        return best

#this one is very similar to number of islands
#but instead you return the count of that island, how many 1's found in that chain

#Time: O(m * n) because goes through entire grid
#Space O(m * n) because recursive stack as a worst case can be all grid elements
