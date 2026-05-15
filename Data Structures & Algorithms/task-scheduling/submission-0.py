class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [0] * 26
        for char in tasks:
            arr[ord(char)-65] += 1
        heap = []
        for num in arr:
            if num != 0:
                heap.append(num)
        heapq.heapify_max(heap)

        queue = deque()
        time = 0
        while heap or queue:
            time += 1
            if heap:
                num = heapq.heappop_max(heap)
                num -= 1
                if num != 0:
                    queue.append((num, time+n))
            if queue:
                task, end_time = queue[0]
                if end_time == time:
                    queue.popleft()
                    heapq.heappush_max(heap, task)
        return time

    
