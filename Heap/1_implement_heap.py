import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        heapq.heappush(self.heap, item)

    def extract_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

# Example usage
heap = MinHeap()
heap.insert(5)
heap.insert(10)
heap.insert(2)
heap.insert(8)

print(heap.extract_min())  # Output: 2
print(heap.extract_min())  # Output: 5
