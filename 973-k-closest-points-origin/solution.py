import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #need to calculate the distance between points and origin
        #and then store distances in a heap
        heap = []

        for x, y in points:
            distance = math.sqrt((x ** 2) + (y ** 2))
            if len(heap) < k:
                heapq.heappush(heap, (-1 * distance, [x, y]))
            elif distance < -1 * heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (-1 * distance, [x, y]))

        return [point for _, point in heap]

            #need k smallest
            #heap of k
            #max heap
            #if i keep a max heap of the lowest values where heap[0] has the greatest lowest

        ''' 
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        '''

#apporach for this one is calculate the distance for each point and store in heap
#use a max heap (so put in negative values) and just push when k has not reached yet, after it has, only pop and push if value is less than the current top
#that way the heap will store the k smallest distances with the greatest distance of that at heap[0]
#push a value if its less than heap[0] meaning heap will always store that same bottom k amount (pop the most, add the new)

#Time: O(n) because go through each point
#Space: O(k) cause holds at most k elements