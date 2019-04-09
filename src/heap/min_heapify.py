import math
class MinHeapify(object):

    def __init__(self, array):
        self.array = array
    
    def build(self):
        array = self.array
        size = len(array)
        for key in reversed(range(math.ceil(size/2))):
            self.min(array, key)

        return array
    
    def min(self, array=None, i=0, heap_size=None):
        array = array or self.array
        n = len(array) if heap_size is None else heap_size
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if n > left and array[left] < array[largest]:
            largest = left

        if n > right and array[right] < array[largest]:
            largest = right
        
        if largest != i:
            temp = array[largest]
            array[largest] = array[i]
            array[i] = temp
            self.min(array, largest, n)
        return array