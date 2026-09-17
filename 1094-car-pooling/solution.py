import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #drop off before pick up
        #cant exceed capacity, if so = return false

        #have two heaps, one for pick ups and one for drop offs
        #both min heaps

        #then iterate through km lengths

        #drop offs first, then pick ups
        #once all empty = True
        #if capacity exceeded at any point = return False


        heap = []
        drop_offs = []


        for passengers, from_km, to_km in trips:
            heapq.heappush(heap, (from_km, to_km, passengers))

        #now all the starting ones are in min heap so first stop first


        i = 0

        car_count = 0

        while heap or drop_offs:
            #check drop_offs first
            while drop_offs and drop_offs[0][0] == i:
                to_k, passengers = heapq.heappop(drop_offs)
                car_count -= passengers



            #check pickups
            while heap and heap[0][0] == i:
                from_k, to_k, passengers = heapq.heappop(heap)
                car_count += passengers
                heapq.heappush(drop_offs, (to_k, passengers))

            if car_count > capacity:
                return False

            
            i += 1

        if car_count or heap or drop_offs:
            return False

        #reaches the end successfully = return True
        return True


"""
approach here is to keep two heaps (one for dropoffs and one for pickups)

#creates pickups as storing (from, to, passengers)
dropoffs will be (to, passengers)

then use a counter to iterate through each "stop"
first popoff from dropoffs
remember to first check if dropoffs exists
then subtract passengers from car count

then for pickups add passengers 
then check capacity, return false if it goes over

Time: O(max stop + nlogn) nlogn for the heap operations, since this problem limits max km to 1000, can just be O(nlogn)
Space: O(n) worst case
"""