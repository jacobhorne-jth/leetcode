class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in dirs:
                nr = dr + r
                nc = dc + c

                dfs(nr, nc)
    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count


#concept for this one is to iterate through the grid, once a island is found:
#increment count
#perform dfs / bfs on it to remove that entire island
#i chose bfs, go in each direaction (up, down, left, right)
#remember to check bounds, and if its actually == 1, if not, jsut return (base case is out of bounds or not island anymore)

#remember to actually set it to water now cause removing the island
#once that entire dfs call is returned, it will keep going, keeping count of total islands found
#key: find island : remove it, increment count

#Time: O(m * n) because go through each
#Space: O(m * n) if counting grid, O(1) if not
#^^^ actually wrong, the dfs recursive call stack uses mem, worst case is every one is in that = O(m * n)