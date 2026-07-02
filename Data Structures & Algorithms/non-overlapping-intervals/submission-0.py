class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        remove = 0
        last = intervals[0][1]

        for i in range(1 , len(intervals)):
            if intervals[i][0] < last:
                remove += 1
            else:
                last = intervals[i][1]
        return remove        


        