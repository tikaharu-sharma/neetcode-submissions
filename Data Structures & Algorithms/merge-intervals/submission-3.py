class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) #sort by start time
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
            else:
                # last = res.pop()
                # newInterval = [min(last[0],intervals[i][0]), max(last[1],intervals[i][1])]
                # res.append(newInterval)
                res[-1][1] = max(res[-1][1], intervals[i][1])
        
        return res

