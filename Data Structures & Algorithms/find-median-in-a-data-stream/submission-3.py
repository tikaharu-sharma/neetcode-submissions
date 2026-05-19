class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxHeap, num)

        if self.maxHeap and self.minHeap and self.maxHeap[0] > self.minHeap[0]:
            a = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, a)
        
        if len(self.maxHeap) - len(self.minHeap) > 1:
            a = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, a)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            a = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, a)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) < len(self.maxHeap):
            return self.maxHeap[0]
        else:
            return (self.minHeap[0]+self.maxHeap[0])/2
        

