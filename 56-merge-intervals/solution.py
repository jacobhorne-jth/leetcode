class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        stack = []

        for start, end in intervals:
            if stack:
                if start <= stack[-1][1]:
                    os, oe = stack.pop()
                    stack.append([os, max(oe, end)])
                    continue

            stack.append([start, end])

        return stack


#basically sort the intervals by start time, if same start time, will have lesser end time first
#create a stack
#iterate for start, end in intervals and if the stack exists, check if the current start <= the end time at the top of the stakc = most recent interval
#if thats true, that means there is an overlap between the two so then you pop it and append the original start one, and then the max of the two end times
#then continue

#if not stack, or no overlap, just append [start, end]

#then return stack because it will have all of the stuff

