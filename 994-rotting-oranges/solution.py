from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque([])
        fresh = 0
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = grid[r][c]

                if val == 0:
                    continue
                elif val == 1:
                    fresh += 1
                else:
                    q.append((r, c, 0))


        #now q contains all rotten oranges
        #and we have a value for total fresh ones to rot

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        highest_v = 0
        while q:
            r, c, v = q.popleft()

            highest_v = max(v, highest_v)

            for dr, dc in directions:
                newr, newc = r + dr, c + dc

                if newr > len(grid) - 1 or newr < 0 or newc > len(grid[0]) - 1 or newc < 0 or grid[newr][newc] == 0 or grid[newr][newc] == 2:
                    continue

                else:
                    grid[newr][newc] = 2
                    fresh -= 1
                    q.append((newr, newc, v + 1))


        
        if fresh == 0:
            return highest_v

        else:
            return -1



#grid of 0, 1, 2
#0 = nothing
#1 = fresh orange
#2 = rotten orange

#every minute a rotten orange spreads one block up down left or right, infecting any fresh oranges if they are there

#need to find the longest amounts of minutes to infect all the fresh oranges

#go through the entire grid, adding rotten oranges coords to a queue
#count fresh oranges

#now queue has all the rotten oranges = starting places for BFS
#while q, pop off and then iterating through directions
#if in bounds and a fresh orange, infect it (change it to 2)
#then add to queue with increased minute

#decrement fresh
#also track highest minute

#(r, c, min)

#at the end when q is empty
#at the end return highest minute if fresh = 0
#otherwise return -1



#Time: O(m*n) worst case cause for initial searching + each cell is processed at most once in the bfs
#Space: O(m*n) worst case if everything is a rotten orange = added to queue