class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        min_heap = self.arr
        heapq.heapify(min_heap)

        length = len(min_heap)
        temp = []

        if length % 2 == 0:
            while len(min_heap) != int(length/2) + 1:
                num = heapq.heappop(min_heap)
                temp.append(num)
            a = heapq.heappop(min_heap)
            temp.append(a)
            b = heapq.heappop(min_heap)
            temp.append(b)
            median = (float(a) + float(b))/2
        else:
            while len(min_heap) != int(length/2) + 1:
                num = heapq.heappop(min_heap)
                temp.append(num)
            median = heapq.heappop(min_heap)
            temp.append(median)
        for item in temp:
            heapq.heappush(min_heap, item)
        return median

