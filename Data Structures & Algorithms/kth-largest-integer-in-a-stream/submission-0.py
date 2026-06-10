from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.arr, val)
        if len(self.arr) > self.k:
            heappop(self.arr)

        return self.arr[0]

        
