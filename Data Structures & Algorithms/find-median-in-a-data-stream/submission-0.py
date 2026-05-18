class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        length = len(self.arr)
        if length % 2 == 0:
            n = int(length/2)
            median = (float(self.arr[n-1])+float(self.arr[n]))/2
        else:
            n = int(length/2)
            median = self.arr[n]
        return median