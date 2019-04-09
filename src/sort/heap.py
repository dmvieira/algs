from src.sort import Sort
from src.heap.max_heapify import MaxHeapify

class HeapSort(Sort):
    
    def sort(self):

        heap = MaxHeapify(self.sample)
        sample = heap.build()
        heap_size = len(sample)
        size = len(sample)
        for i in reversed(range(size)):
            sample[i], sample[0] = sample[0], sample[i]
            heap_size-=1
            sample = heap.max(sample, 0, heap_size)
        return sample