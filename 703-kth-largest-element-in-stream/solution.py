import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        #min heap of size k
        for n in nums:
            heapq.heappush(self.heap, n)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

        

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


#use a min heap to store k elements
#since its a min heap, it will store the kth largest element at the head
#key thing is always ensuring its not over k elements AFTER adding the new one


#Time: O(n) for creation, O(logn) for insertion cause heapify
#Space: O(k) cause k elements stored in a heap