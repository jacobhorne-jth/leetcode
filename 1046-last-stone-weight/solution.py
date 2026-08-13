import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #keep max heap and always pop top two
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            x, y = -1 * heapq.heappop(heap), -1 * heapq.heappop(heap)

            if x == y:
                continue

            new = max(x, y) - min(x,y)
            heapq.heappush(heap, -new)
        
        if not heap:
            return 0

        return -1 * heap[0]

#for this one, keep a max heap to store the max weight at the top
#do that with -negative
#then simply pop the top two (the two most)
#if they are equal continue
#if they arent, set the new amt to the difference in weight between most and less
#add that back into heap
#key thing here is remembering negatives

#Time: O(n) because inserting all into the heap initially
#Space: O(n) because all are in the heap at the start


        