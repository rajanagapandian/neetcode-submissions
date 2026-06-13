from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [stone * -1 for stone in stones]
        heapify(arr)
        while len(arr) > 1:
            x, y = heappop(arr), heappop(arr)
            diff = -x - (-y)
            if not diff == 0:
                heappush(arr, -diff)
        
        return -arr[0] if len(arr) else 0