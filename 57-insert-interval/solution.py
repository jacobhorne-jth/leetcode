class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []

        newStart, newEnd = newInterval

        

        #three phases
        #everything before
        while i < len(intervals) and intervals[i][1] < newStart:
            res.append(intervals[i])
            i += 1
        

        #everything that overlaps
        while i < len(intervals) and intervals[i][0] <= newEnd:
            newStart = min(newStart, intervals[i][0])
            newEnd = max(newEnd, intervals[i][1])
            i += 1

        res.append([newStart, newEnd])

    
        #everything after
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res


#split into 3 phases
#everything before
#everything overlapping
#and everything after

#before and after are simple while loops

#before:
# - intervals[i][1] < newStart checks to make sure the interval is completely before the one we are inserting
#everything that overlaps
#is different, just use curr start <= inserting intervals end
# - intervals[i][0] <= newEnd: now its no longer completely before so this is the right bound
# while the start is less than the newend means overlap
# once start is more than newEnd its the third phase 

#because if the curr start is <= what we are trying to inserts end 
#that means there is overlap
#track the minimum and maximum start and ends
#append that

#then do the final one


#Time: O(n) because goes through each interval pair once
#Space: O(n) because result list contains n + 1 items or O(n)