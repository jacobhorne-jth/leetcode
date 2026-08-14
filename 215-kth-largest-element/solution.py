import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)
        return heap[0]

        #keep a min heap of size k, only pop and push if greater than heap[0]


#very very similar to the closest points to origin
#this time keep a min heap of the top largest window
#that way the minimum of that would be the return value
#if not at k elements yet, just push
#otherwise only pop and push when the new value is greater than heap[0] - the smallest of the largest k